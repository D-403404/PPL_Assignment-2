Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite
Then type: python run.py test ASTGenSuite

Note: Edited ZCode.g4 - Linked rules (2 versions)
- newlineLst_0, newlineLst_1                => removed
- arrayElement, op_unary_index, expr_index
- arrayId, stmt_array_declaration, param
- BOOL  => moved above IDENTIFIER
- expr_func_call (new), operand