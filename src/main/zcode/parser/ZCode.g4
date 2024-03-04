// Nguyễn Thành Đạt - 2152506

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: declarationLst EOF;
declarationLst: newlineLst_0 stmt_declaration declarationLst | newlineLst_0 stmt_declaration;

newlineLst_0: SB_NEWLINE newlineLst_0 | ;
newlineLst_1: SB_NEWLINE newlineLst_1 | SB_NEWLINE;

COMMENT: '##' ~('\r' | '\n')* -> skip;
WS: [ \t\b\f]+ -> skip; // skip spaces, tabs, backspaces, form feeds
WS2: (' ' | '\\t' | '\\b' | '\\f')+ -> skip;

//=====SYMBOLS=====
SB_LEFTBRACKET: '(';
SB_RIGHTBRACKET: ')';
SB_LEFTSQUARE: '[';
SB_RIGHTSQUARE: ']';
SB_COMMA: ',';
SB_NEWLINE: ('\r' '\n' | '\r' | '\n' | '\\n') {self.text = self.text.replace('\r\n','\n').replace('\r','\n')};
SB_CR: '\\r';

//=====KEYWORDS=====
fragment KW_TRUE: 'true';
fragment KW_FALSE: 'false';
KW_NUMBER: 'number';
KW_BOOL: 'bool';
KW_STRING: 'string';
KW_RETURN: 'return';
KW_VAR: 'var';
KW_DYNAMIC: 'dynamic';
KW_FUNC: 'func';
KW_FOR: 'for';
KW_UNTIL: 'until';
KW_BY: 'by';
KW_BREAK: 'break';
KW_CONTINUE: 'continue';
KW_IF: 'if';
KW_ELSE: 'else';
KW_ELIF: 'elif';
KW_BEGIN: 'begin';
KW_END: 'end';

//=====OPERATORS=====
OP_PLUS: '+';
OP_MINUS: '-';
OP_MULT: '*';
OP_DIV: '/';
OP_MOD: '%';
OP_ASSIGN: '<-';
OP_EQUAL_NUM: '=';
OP_UNEQUAL: '!=';
OP_LESS: '<';
OP_MORE: '>';
OP_LESSOREQUAL: '<=';
OP_MOREOREQUAL: '>=';
OP_CONCAT: '...';
OP_EQUAL_STR: '==';
OP_NOT: 'not';
OP_AND: 'and';
OP_OR: 'or';

//=====LITERALS=====
IDENTIFIER: [A-Za-z_] [A-Za-z_0-9]*;
NUMBER: IntPart DecPart? ExpPart?;
fragment Digit: [0-9];
fragment IntPart: Digit+;
fragment DecPart: '.' Digit*;
fragment ExpPart: [Ee] [+-]? Digit+;
BOOL: KW_TRUE | KW_FALSE;
STRING:
	'"' StringContent '"' {self.text = self.text[1:-1]};
fragment StringContent: (
		~('"' | '\\' | '\n' | '\r')
		| EscSequence
		| '\'"'
	)*;
fragment EscSequence:
	'\\b'
	| '\\t'
	| '\\f'
	| '\\r'
	| '\\\''
	| '\\\\';

//=====EXPRESSIONS=====
// ===Array===
arrayElement: IDENTIFIER expr_element | stmt_func_call expr_element;
expr_element: SB_LEFTSQUARE op_index SB_RIGHTSQUARE;
op_index: expr SB_COMMA op_index | expr;

//Precedence: high to low
op_unary_index: arrayElement;
op_unary_sign: OP_MINUS;
op_unary_logical: OP_NOT;
op_binary_multiplying: OP_MULT | OP_DIV | OP_MOD;
op_binary_adding: OP_PLUS | OP_MINUS;
op_binary_logical: OP_AND | OP_OR;
op_binary_relational:
	OP_EQUAL_NUM
	| OP_EQUAL_STR
	| OP_UNEQUAL
	| OP_LESS
	| OP_MORE
	| OP_LESSOREQUAL
	| OP_MOREOREQUAL;
op_binary_string: OP_CONCAT;

expr: expr_string;
expr_string: expr_relational op_binary_string expr_relational | expr_relational;
expr_relational: expr_logical op_binary_relational expr_logical | expr_logical;
expr_logical: expr_logical op_binary_logical expr_adding | expr_adding;
expr_adding: expr_adding op_binary_adding expr_multiplying | expr_multiplying;
expr_multiplying: expr_multiplying op_binary_multiplying expr_not | expr_not;
expr_not: op_unary_logical expr_not | expr_sign;
expr_sign: op_unary_sign expr_sign | expr_index;
expr_index: op_unary_index | operand;
operand: IDENTIFIER | NUMBER | BOOL | STRING | arrayValue | stmt_func_call | SB_LEFTBRACKET expr SB_RIGHTBRACKET;

//=====VARIABLES=====
kw_type_explicit: KW_NUMBER | KW_BOOL | KW_STRING;
kw_type: kw_type_explicit | KW_VAR | KW_DYNAMIC;
stmt_declaration: 
		stmt_var_declaration newlineLst_1 
		| stmt_array_declaration newlineLst_1 
		| stmt_func_declaration newlineLst_1
		;

stmt_var_declaration: stmt_var_declaration_explicit | stmt_var_declaration_dynamic | stmt_var_declaration_var;
stmt_var_declaration_explicit: kw_type_explicit IDENTIFIER value_init | kw_type_explicit IDENTIFIER;
stmt_var_declaration_dynamic: KW_DYNAMIC IDENTIFIER value_init | KW_DYNAMIC IDENTIFIER;
stmt_var_declaration_var: KW_VAR IDENTIFIER value_init;
value_init: OP_ASSIGN expr;

stmt_array_declaration: kw_type_explicit arrayId array_init | kw_type_explicit arrayId;
arrayId: IDENTIFIER SB_LEFTSQUARE arrayDim SB_RIGHTSQUARE;
arrayDim: NUMBER SB_COMMA arrayDim | NUMBER;
array_init: OP_ASSIGN arrayValue;
arrayValue: SB_LEFTSQUARE exprLst SB_RIGHTSQUARE;
exprLst: expr SB_COMMA exprLst | expr;

stmt_func_declaration:
	KW_FUNC IDENTIFIER SB_LEFTBRACKET paramLst SB_RIGHTBRACKET newlineLst_0 func_body;	
paramLst: param paramLstTail | ;
paramLstTail: SB_COMMA param paramLstTail | ;
param: kw_type_explicit IDENTIFIER | kw_type_explicit arrayId;
func_body: stmt_return | stmt_block | ;

//=====STATEMENTS=====
statement_type:
		stmt_var_declaration newlineLst_1 
		| stmt_array_declaration newlineLst_1
		| stmt_assignment newlineLst_1
		| stmt_if							// No newline to prevent double newline from the stmt and its body
		| stmt_for							// No newline to prevent double newline from the stmt and its body
		| stmt_break newlineLst_1
		| stmt_continue newlineLst_1
		| stmt_return newlineLst_1
		| stmt_func_call newlineLst_1
		| stmt_block newlineLst_1
		;
statement: statement_type;

//===Assignment===
stmt_assignment: assignment_lhs value_init;
assignment_lhs: IDENTIFIER | arrayElement;

//===If statement===
if_statement:
	KW_IF SB_LEFTBRACKET expr SB_RIGHTBRACKET newlineLst_0 statement;
elif_statement:
	KW_ELIF SB_LEFTBRACKET expr SB_RIGHTBRACKET newlineLst_0 statement;
else_statement: KW_ELSE newlineLst_0 statement | ;
stmt_if:
	if_statement newlineLst_0 elifLst else_statement;
elifLst: elif_statement newlineLst_0 elifLst | ;

//===For statement===
stmt_for:
	KW_FOR IDENTIFIER KW_UNTIL expr KW_BY expr newlineLst_0
		statement;

stmt_break: KW_BREAK;
stmt_continue: KW_CONTINUE;
stmt_return: KW_RETURN expr | KW_RETURN;

//===Function call statement===
stmt_func_call:
	IDENTIFIER SB_LEFTBRACKET argLst SB_RIGHTBRACKET;
argLst: expr argLstTail | ;
argLstTail: SB_COMMA expr argLstTail | ;

//===Block statement===
stmt_block: KW_BEGIN newlineLst_1 statementLst KW_END;
statementLst: statement statementLst | ;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' StringContent ('\r' | '\n' | '\\n' | EOF) {self.text = self.text[1:].replace('\r','').replace('\n','').replace('\\n',''); raise UncloseString(self.text)};
ILLEGAL_ESCAPE: '"' StringContent ('\\' ~[bfrnt'\\]) {self.text = self.text[1:]; raise IllegalEscape(self.text)};