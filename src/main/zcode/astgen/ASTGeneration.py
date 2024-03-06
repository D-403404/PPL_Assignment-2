from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    # def visitProgram(self, ctx: ZCodeParser.ProgramContext):
    #     return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.declarationLst()))
    
    def visitDeclarationLst(self, ctx: ZCodeParser.DeclarationLstContext):
        if ctx.declarationLst():
            return [self.visit(ctx.stmt_declaration())] + self.visit(ctx.declarationLst())
        else:
            return [self.visit(ctx.stmt_declaration())]
    
    # def visitNewlineLst_0(self, ctx: ZCodeParser.NewlineLst_0Context):
    #     return None
    
    # def visitNewlineLst_1(self, ctx: ZCodeParser.NewlineLst_1Context):
    #     return None
    


    def visitArrayElement(self, ctx: ZCodeParser.ArrayElementContext):
        if ctx.IDENTIFIER():
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr_element()))
        elif ctx.stmt_func_call():
            return ArrayCell(self.visit(ctx.Stmt_func_call()), self.visit(ctx.expr_element()))
        # return ArrayCell(self.visit(ctx.operand()), self.visit(ctx.expr_element()))
    
    def visitExpr_element(self, ctx: ZCodeParser.Expr_elementContext):
        return self.visit(ctx.op_index())
    
    def visitOp_index(self, ctx: ZCodeParser.Op_indexContext):
        if ctx.op_index():
            return [self.visit(ctx.expr())] + self.visit(ctx.op_index())
        else:
            return [self.visit(ctx.expr())]
    

    
    def visitOp_unary_index(self, ctx: ZCodeParser.Op_unary_indexContext):
        return self.visit(ctx.arrayElement())
        # return self.visit(ctx.expr_element())
    
    def visitOp_unary_sign(self, ctx: ZCodeParser.Op_unary_signContext):
        return ctx.OP_MINUS().getText()
    
    def visitOp_unary_logical(self, ctx: ZCodeParser.Op_unary_logicalContext):
        return ctx.OP_NOT().getText()
    
    def visitOp_binary_multiplying(self, ctx: ZCodeParser.Op_binary_multiplyingContext):
        if ctx.OP_MULT():
            return ctx.OP_MULT().getText()
        elif ctx.OP_DIV():
            return ctx.OP_DIV().getText()
        else:
            return ctx.OP_MOD().getText()
    
    def visitOp_binary_adding(self, ctx: ZCodeParser.Op_binary_addingContext):
        if ctx.OP_PLUS():
            return ctx.OP_PLUS().getText()
        else:
            return ctx.OP_MINUS().getText()
    
    def visitOp_binary_logical(self, ctx: ZCodeParser.Op_binary_logicalContext):
        if ctx.OP_AND():
            return ctx.OP_AND().getText()
        else:
            return ctx.OP_OR().getText()
    
    def visitOp_binary_relational(self, ctx: ZCodeParser.Op_binary_relationalContext):
        if ctx.OP_EQUAL_NUM():
            return ctx.OP_EQUAL_NUM().getText()
        elif ctx.OP_EQUAL_STR():
            return ctx.OP_EQUAL_STR().getText()
        elif ctx.OP_UNEQUAL():
            return ctx.OP_UNEQUAL().getText()
        elif ctx.OP_LESS():
            return ctx.OP_LESS().getText()
        elif ctx.OP_MORE():
            return ctx.OP_MORE().getText()
        elif ctx.OP_LESSOREQUAL():
            return ctx.OP_LESSOREQUAL().getText()
        else:
            return ctx.OP_MOREOREQUAL().getText()
    
    def visitOp_binary_string(self, ctx: ZCodeParser.Op_binary_stringContext):
        return ctx.OP_CONCAT().getText()
    


    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        return self.visit(ctx.expr_string())
    
    def visitExpr_string(self, ctx: ZCodeParser.Expr_stringContext):
        if ctx.op_binary_string():
            return BinaryOp(self.visit(ctx.op_binary_string()), self.visit(ctx.expr_relational(0)), self.visit(ctx.expr_relational(1)))
        else:
            return self.visit(ctx.expr_relational())
    
    def visitExpr_relational(self, ctx: ZCodeParser.Expr_relationalContext):
        if ctx.op_binary_relational():
            return BinaryOp(self.visit(ctx.op_binary_relational()), self.visit(ctx.expr_logical(0)), self.visit(ctx.expr_logical(1)))
        else:
            return self.visit(ctx.expr_logical())
    
    def visitExpr_logical(self, ctx: ZCodeParser.Expr_logicalContext):
        if ctx.op_binary_logical():
            return BinaryOp(self.visit(ctx.op_binary_logical()), self.visit(ctx.expr_logical()), self.visit(ctx.expr_adding()))
        else:
            return self.visit(ctx.expr_adding())
    
    def visitExpr_adding(self, ctx: ZCodeParser.Expr_addingContext):
        if ctx.op_binary_adding():
            return BinaryOp(self.visit(ctx.op_binary_adding()), self.visit(ctx.expr_adding()), self.visit(ctx.expr_multiplying()))
        else:
            return self.visit(ctx.expr_multiplying())
    
    def visitExpr_multiplying(self, ctx: ZCodeParser.Expr_multiplyingContext):
        if ctx.op_binary_multiplying():
            return BinaryOp(self.visit(ctx.op_binary_multiplying()), self.visit(ctx.expr_multiplying()), self.visit(ctx.expr_not()))
        else:
            return self.visit(ctx.expr_not())
    
    def visitExpr_not(self, ctx: ZCodeParser.Expr_notContext):
        if ctx.op_unary_logical():
            return UnaryOp(self.visit(ctx.op_unary_logical()), self.visit(ctx.expr_not()))
        else:
            return self.visit(ctx.expr_sign())
    
    def visitExpr_sign(self, ctx: ZCodeParser.Expr_signContext):
        if ctx.op_unary_sign():
            return UnaryOp(self.visit(ctx.op_unary_sign()), self.visit(ctx.expr_sign()))
        else:
            return self.visit(ctx.expr_index())
    
    def visitExpr_index(self, ctx: ZCodeParser.Expr_indexContext):
        if ctx.op_unary_index():
            return self.visit(ctx.op_unary_index())
        else:
            return self.visit(ctx.operand())
        # if ctx.op_unary_index():
        #     return UnaryOp(self.visit(ctx.op_unary_index()), self.visit(ctx.operand()))
        # else:
        #     return self.visit(ctx.operand())
    
    def visitOperand(self, ctx: ZCodeParser.OperandContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.NUMBER():
            return NumberLiteral(float(ctx.NUMBER().getText()))
        elif ctx.BOOL():
            return BooleanLiteral(eval(ctx.BOOL().getText()))
        elif ctx.STRING():
            return StringLiteral(float(ctx.STRING().getText()))
        elif ctx.arrayValue():
            return self.visit(ctx.arrayValue())
        elif ctx.stmt_func_call():
            return self.visit(ctx.stmt_func_call())
        else:
            return self.visit(ctx.expr())
    


    def visitKw_type_explicit(self, ctx: ZCodeParser.Kw_type_explicitContext):
        if ctx.KW_NUMBER():
            return NumberType()
        elif ctx.KW_BOOL():
            return BoolType()
        else:
            return StringType()
    
    def visitKw_type(self, ctx: ZCodeParser.Kw_typeContext):
        if ctx.kw_type_explicit():
            return self.visit(ctx.kw_type_explicit())
        elif ctx.KW_VAR():
            return ctx.KW_VAR().getText()
        else:
            return ctx.KW_DYNAMIC().getText()
    
    def visitStmt_declaration(self, ctx: ZCodeParser.Stmt_declarationContext):
        if ctx.stmt_var_declaration():
            return self.visit(ctx.stmt_var_declaration())
        elif ctx.stmt_array_declaration():
            return self.visit(ctx.stmt_array_declaration())
        else:
            return self.visit(ctx.stmt_func_declaration())
    


    def visitStmt_var_declaration(self, ctx: ZCodeParser.Stmt_var_declarationContext):
        if ctx.stmt_var_declaration_explicit():
            return self.visit(ctx.stmt_var_declaration_explicit())
        elif ctx.stmt_var_declaration_dynamic():
            return self.visit(ctx.stmt_var_declaration_dynamic())
        else:
            return self.visit(ctx.stmt_var_declaration_var())
    
    def visitStmt_var_declaration_explicit(self, ctx: ZCodeParser.Stmt_var_declaration_explicitContext):
        if ctx.value_init():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.kw_type_explicit()), None, self.visit(ctx.value_init()))
        else:
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.kw_type_explicit()), None, None)
    
    def visitStmt_var_declaration_dynamic(self, ctx: ZCodeParser.Stmt_var_declaration_dynamicContext):
        if ctx.value_init():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.KW_DYNAMIC().getText(), self.visit(ctx.value_init()))
        else:
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.KW_DYNAMIC().getText(), None)
    
    def visitStmt_var_declaration_var(self, ctx: ZCodeParser.Stmt_var_declaration_varContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.KW_VAR().getText(), self.visit(ctx.value_init()))
    
    def visitValue_init(self, ctx: ZCodeParser.Value_initContext):
        return self.visit(ctx.expr())
    


    def visitStmt_array_declaration(self, ctx: ZCodeParser.Stmt_array_declarationContext):
        array_id = self.visit(ctx.arrayId())
        if ctx.array_init():
            return VarDecl(array_id[0], ArrayType(array_id[1], self.visit(ctx.kw_type_explicit())), None, self.visit(ctx.array_init()))
        else:
            return VarDecl(array_id[0], ArrayType(array_id[1], self.visit(ctx.kw_type_explicit())), None, None)
        # if ctx.array_init():
        #     return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.arrayDim()), self.visit(ctx.kw_type_explicit())), None, self.visit(ctx.array_init()))
        # else:
        #     return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.arrayDim()), self.visit(ctx.kw_type_explicit())), None, None)
    
    def visitArrayId(self, ctx: ZCodeParser.ArrayIdContext):
        return Id(ctx.IDENTIFIER().getText()), self.visit(ctx.arrayDim()) 
    
    def visitArrayDim(self, ctx: ZCodeParser.ArrayDimContext):
        if ctx.arrayDim():
            return [NumberLiteral(float(ctx.NUMBER().getText()))] + self.visit(ctx.arrayDim())
        else:
            return [NumberLiteral(float(ctx.NUMBER().getText()))]
    
    def visitArray_init(self, ctx: ZCodeParser.Array_initContext):
        return self.visit(ctx.arrayValue())
    
    def visitArrayValue(self, ctx: ZCodeParser.ArrayValueContext):
        return ArrayLiteral(self.visit(ctx.exprLst()))
    
    def visitExprLst(self, ctx: ZCodeParser.ExprLstContext):
        if ctx.exprLst():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprLst())
        else:
            return [self.visit(ctx.expr())]
    


    def visitStmt_func_declaration(self, ctx: ZCodeParser.Stmt_func_declarationContext):
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.paramLst()), self.visit(ctx.func_body()))
    
    def visitParamLst(self, ctx: ZCodeParser.ParamLstContext):
        if ctx.paramLst():
            return [self.visit(ctx.param())] + self.visit(ctx.paramLst())
        else:
            return []
    
    def visitParamLstTail(self, ctx: ZCodeParser.ParamLstTailContext):
        if ctx.paramLstTail():
            return [self.visit(ctx.param())] + self.visit(ctx.paramLst())
        else:
            return []
    
    def visitParam(self, ctx: ZCodeParser.ParamContext):
        if not ctx.arrayId():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.kw_type_explicit()), None, None)
        else:
            array_id = self.visit(ctx.arrayId())
            return VarDecl(array_id[0], ArrayType(array_id[1], self.visit(ctx.kw_type_explicit())), None, None)
        # if not ctx.arrayDim():
        #     return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.kw_type_explicit()), None, None)
        # else:
        #     return VarDecl(ArrayType(self.visit(ctx.arrayDim()), self.visit(ctx.kw_type_explicit())), self.visit(ctx.kw_type_explicit()), None, None)
    
    def visitFunc_body(self, ctx: ZCodeParser.Func_bodyContext):
        if ctx.stmt_return():
            return self.visit(ctx.stmt_return())
        elif ctx.stmt_block():
            return self.visit(ctx.stmt_block())
        else:
            return None
    


    # def visitStatement_type(self, ctx: ZCodeParser.Statement_typeContext):
    #     return None
    
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        if ctx.stmt_var_declaration():
            return self.visit(ctx.stmt_var_declaration())
        elif ctx.stmt_array_declaration():
            return self.visit(ctx.stmt_array_declaration())
        elif ctx.stmt_assignment():
            return self.visit(ctx.stmt_assignment())
        elif ctx.stmt_if():
            return self.visit(ctx.stmt_if())
        elif ctx.stmt_for():
            return self.visit(ctx.stmt_for())
        elif ctx.stmt_break():
            return self.visit(ctx.stmt_break())
        elif ctx.stmt_continue():
            return self.visit(ctx.stmt_continue())
        elif ctx.stmt_return():
            return self.visit(ctx.stmt_return())
        elif ctx.stmt_func_call():
            return self.visit(ctx.stmt_func_call())
        else:
            return self.visit(ctx.stmt_block())
    


    def visitStmt_assignment(self, ctx: ZCodeParser.Stmt_assignmentContext):
        return Assign(self.visit(ctx.assignment_lhs()), self.visit(ctx.value_init()))
    
    def visitAssignment_lhs(self, ctx: ZCodeParser.Assignment_lhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.arrayElement())



    def visitIf_statement(self, ctx: ZCodeParser.If_statementContext):
        return self.visit(ctx.expr()), self.visit(ctx.statement())
    
    def visitElif_statement(self, ctx: ZCodeParser.Elif_statementContext):
        return self.visit(ctx.expr()), self.visit(ctx.statement())
    
    def visitElse_statement(self, ctx: ZCodeParser.Else_statementContext):
        return self.visit(ctx.statement())
    
    def visitStmt_if(self, ctx: ZCodeParser.Stmt_ifContext):
        # return If(self.visit(ctx.if_statement())[0], self.visit(ctx.if_statement())[1], self.visit(ctx.elifLst()), self.visit(ctx.else_statement()))
        if_stmt = self.visit(ctx.if_statement())
        return If(if_stmt[0], if_stmt[1], self.visit(ctx.elifLst()), self.visit(ctx.else_statement()))
    
    def visitElifLst(self, ctx: ZCodeParser.ElifLstContext):
        if ctx.elifLst():
            return [self.visit(ctx.elif_statement())] + self.visit(ctx.elifLst())
        else:
            return []
    


    def visitStmt_for(self, ctx: ZCodeParser.Stmt_forContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.statement()))
    
    
    
    def visitStmt_break(self, ctx: ZCodeParser.Stmt_breakContext):
        return Break()
    
    def visitStmt_continue(self, ctx: ZCodeParser.Stmt_continueContext):
        return Continue()
    
    def visitStmt_return(self, ctx: ZCodeParser.Stmt_returnContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return(None)
    
    
    
    def visitStmt_func_call(self, ctx: ZCodeParser.Stmt_func_callContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.argLst()))
    
    def visitArgLst(self, ctx: ZCodeParser.ArgLstContext):
        if ctx.argLstTail():
            return [self.visit(ctx.expr())] + self.visit(ctx.argLstTail())
        else:
            return []
    
    def visitArgLstTail(self, ctx: ZCodeParser.ArgLstTailContext):
        if ctx.argLstTail():
            return [self.visit(ctx.expr())] + self.visit(ctx.argLstTail())
        else:
            return []
    


    def visitStmt_block(self, ctx: ZCodeParser.Stmt_blockContext):
        return Block(self.visit(ctx.statementLst()))
    
    def visitStatementLst(self, ctx: ZCodeParser.StatementLstContext):
        if ctx.statementLst():
            return [self.visit(ctx.statement())] + self.visit(ctx.statementLst())
        else:
            return []