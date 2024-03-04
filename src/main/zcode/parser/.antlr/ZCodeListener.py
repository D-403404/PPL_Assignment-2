# Generated from d://Code scripts//Principles of Programming Languages//PPL_AS2//assignment2//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declarationLst.
    def enterDeclarationLst(self, ctx:ZCodeParser.DeclarationLstContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declarationLst.
    def exitDeclarationLst(self, ctx:ZCodeParser.DeclarationLstContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newlineLst_0.
    def enterNewlineLst_0(self, ctx:ZCodeParser.NewlineLst_0Context):
        pass

    # Exit a parse tree produced by ZCodeParser#newlineLst_0.
    def exitNewlineLst_0(self, ctx:ZCodeParser.NewlineLst_0Context):
        pass


    # Enter a parse tree produced by ZCodeParser#newlineLst_1.
    def enterNewlineLst_1(self, ctx:ZCodeParser.NewlineLst_1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#newlineLst_1.
    def exitNewlineLst_1(self, ctx:ZCodeParser.NewlineLst_1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayElement.
    def enterArrayElement(self, ctx:ZCodeParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayElement.
    def exitArrayElement(self, ctx:ZCodeParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_element.
    def enterExpr_element(self, ctx:ZCodeParser.Expr_elementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_element.
    def exitExpr_element(self, ctx:ZCodeParser.Expr_elementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#op_index.
    def enterOp_index(self, ctx:ZCodeParser.Op_indexContext):
        pass

    # Exit a parse tree produced by ZCodeParser#op_index.
    def exitOp_index(self, ctx:ZCodeParser.Op_indexContext):
        pass


    # Enter a parse tree produced by ZCodeParser#op_unary_index.
    def enterOp_unary_index(self, ctx:ZCodeParser.Op_unary_indexContext):
        pass

    # Exit a parse tree produced by ZCodeParser#op_unary_index.
    def exitOp_unary_index(self, ctx:ZCodeParser.Op_unary_indexContext):
        pass


    # Enter a parse tree produced by ZCodeParser#op_unary_sign.
    def enterOp_unary_sign(self, ctx:ZCodeParser.Op_unary_signContext):
        pass

    # Exit a parse tree produced by ZCodeParser#op_unary_sign.
    def exitOp_unary_sign(self, ctx:ZCodeParser.Op_unary_signContext):
        pass


    # Enter a parse tree produced by ZCodeParser#op_unary_logical.
    def enterOp_unary_logical(self, ctx:ZCodeParser.Op_unary_logicalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#op_unary_logical.
    def exitOp_unary_logical(self, ctx:ZCodeParser.Op_unary_logicalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#op_binary_multiplying.
    def enterOp_binary_multiplying(self, ctx:ZCodeParser.Op_binary_multiplyingContext):
        pass

    # Exit a parse tree produced by ZCodeParser#op_binary_multiplying.
    def exitOp_binary_multiplying(self, ctx:ZCodeParser.Op_binary_multiplyingContext):
        pass


    # Enter a parse tree produced by ZCodeParser#op_binary_adding.
    def enterOp_binary_adding(self, ctx:ZCodeParser.Op_binary_addingContext):
        pass

    # Exit a parse tree produced by ZCodeParser#op_binary_adding.
    def exitOp_binary_adding(self, ctx:ZCodeParser.Op_binary_addingContext):
        pass


    # Enter a parse tree produced by ZCodeParser#op_binary_logical.
    def enterOp_binary_logical(self, ctx:ZCodeParser.Op_binary_logicalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#op_binary_logical.
    def exitOp_binary_logical(self, ctx:ZCodeParser.Op_binary_logicalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#op_binary_relational.
    def enterOp_binary_relational(self, ctx:ZCodeParser.Op_binary_relationalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#op_binary_relational.
    def exitOp_binary_relational(self, ctx:ZCodeParser.Op_binary_relationalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#op_binary_string.
    def enterOp_binary_string(self, ctx:ZCodeParser.Op_binary_stringContext):
        pass

    # Exit a parse tree produced by ZCodeParser#op_binary_string.
    def exitOp_binary_string(self, ctx:ZCodeParser.Op_binary_stringContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr.
    def enterExpr(self, ctx:ZCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr.
    def exitExpr(self, ctx:ZCodeParser.ExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_string.
    def enterExpr_string(self, ctx:ZCodeParser.Expr_stringContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_string.
    def exitExpr_string(self, ctx:ZCodeParser.Expr_stringContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_relational.
    def enterExpr_relational(self, ctx:ZCodeParser.Expr_relationalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_relational.
    def exitExpr_relational(self, ctx:ZCodeParser.Expr_relationalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_logical.
    def enterExpr_logical(self, ctx:ZCodeParser.Expr_logicalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_logical.
    def exitExpr_logical(self, ctx:ZCodeParser.Expr_logicalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_adding.
    def enterExpr_adding(self, ctx:ZCodeParser.Expr_addingContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_adding.
    def exitExpr_adding(self, ctx:ZCodeParser.Expr_addingContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_multiplying.
    def enterExpr_multiplying(self, ctx:ZCodeParser.Expr_multiplyingContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_multiplying.
    def exitExpr_multiplying(self, ctx:ZCodeParser.Expr_multiplyingContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_not.
    def enterExpr_not(self, ctx:ZCodeParser.Expr_notContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_not.
    def exitExpr_not(self, ctx:ZCodeParser.Expr_notContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_sign.
    def enterExpr_sign(self, ctx:ZCodeParser.Expr_signContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_sign.
    def exitExpr_sign(self, ctx:ZCodeParser.Expr_signContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_index.
    def enterExpr_index(self, ctx:ZCodeParser.Expr_indexContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_index.
    def exitExpr_index(self, ctx:ZCodeParser.Expr_indexContext):
        pass


    # Enter a parse tree produced by ZCodeParser#operand.
    def enterOperand(self, ctx:ZCodeParser.OperandContext):
        pass

    # Exit a parse tree produced by ZCodeParser#operand.
    def exitOperand(self, ctx:ZCodeParser.OperandContext):
        pass


    # Enter a parse tree produced by ZCodeParser#kw_type_explicit.
    def enterKw_type_explicit(self, ctx:ZCodeParser.Kw_type_explicitContext):
        pass

    # Exit a parse tree produced by ZCodeParser#kw_type_explicit.
    def exitKw_type_explicit(self, ctx:ZCodeParser.Kw_type_explicitContext):
        pass


    # Enter a parse tree produced by ZCodeParser#kw_type.
    def enterKw_type(self, ctx:ZCodeParser.Kw_typeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#kw_type.
    def exitKw_type(self, ctx:ZCodeParser.Kw_typeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_declaration.
    def enterStmt_declaration(self, ctx:ZCodeParser.Stmt_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_declaration.
    def exitStmt_declaration(self, ctx:ZCodeParser.Stmt_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_var_declaration.
    def enterStmt_var_declaration(self, ctx:ZCodeParser.Stmt_var_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_var_declaration.
    def exitStmt_var_declaration(self, ctx:ZCodeParser.Stmt_var_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_var_declaration_explicit.
    def enterStmt_var_declaration_explicit(self, ctx:ZCodeParser.Stmt_var_declaration_explicitContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_var_declaration_explicit.
    def exitStmt_var_declaration_explicit(self, ctx:ZCodeParser.Stmt_var_declaration_explicitContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_var_declaration_dynamic.
    def enterStmt_var_declaration_dynamic(self, ctx:ZCodeParser.Stmt_var_declaration_dynamicContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_var_declaration_dynamic.
    def exitStmt_var_declaration_dynamic(self, ctx:ZCodeParser.Stmt_var_declaration_dynamicContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_var_declaration_var.
    def enterStmt_var_declaration_var(self, ctx:ZCodeParser.Stmt_var_declaration_varContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_var_declaration_var.
    def exitStmt_var_declaration_var(self, ctx:ZCodeParser.Stmt_var_declaration_varContext):
        pass


    # Enter a parse tree produced by ZCodeParser#value_init.
    def enterValue_init(self, ctx:ZCodeParser.Value_initContext):
        pass

    # Exit a parse tree produced by ZCodeParser#value_init.
    def exitValue_init(self, ctx:ZCodeParser.Value_initContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_array_declaration.
    def enterStmt_array_declaration(self, ctx:ZCodeParser.Stmt_array_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_array_declaration.
    def exitStmt_array_declaration(self, ctx:ZCodeParser.Stmt_array_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayId.
    def enterArrayId(self, ctx:ZCodeParser.ArrayIdContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayId.
    def exitArrayId(self, ctx:ZCodeParser.ArrayIdContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayDim.
    def enterArrayDim(self, ctx:ZCodeParser.ArrayDimContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayDim.
    def exitArrayDim(self, ctx:ZCodeParser.ArrayDimContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_init.
    def enterArray_init(self, ctx:ZCodeParser.Array_initContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_init.
    def exitArray_init(self, ctx:ZCodeParser.Array_initContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayValue.
    def enterArrayValue(self, ctx:ZCodeParser.ArrayValueContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayValue.
    def exitArrayValue(self, ctx:ZCodeParser.ArrayValueContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exprLst.
    def enterExprLst(self, ctx:ZCodeParser.ExprLstContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exprLst.
    def exitExprLst(self, ctx:ZCodeParser.ExprLstContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_func_declaration.
    def enterStmt_func_declaration(self, ctx:ZCodeParser.Stmt_func_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_func_declaration.
    def exitStmt_func_declaration(self, ctx:ZCodeParser.Stmt_func_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramLst.
    def enterParamLst(self, ctx:ZCodeParser.ParamLstContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramLst.
    def exitParamLst(self, ctx:ZCodeParser.ParamLstContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramLstTail.
    def enterParamLstTail(self, ctx:ZCodeParser.ParamLstTailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramLstTail.
    def exitParamLstTail(self, ctx:ZCodeParser.ParamLstTailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param.
    def enterParam(self, ctx:ZCodeParser.ParamContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param.
    def exitParam(self, ctx:ZCodeParser.ParamContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_body.
    def enterFunc_body(self, ctx:ZCodeParser.Func_bodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_body.
    def exitFunc_body(self, ctx:ZCodeParser.Func_bodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement_type.
    def enterStatement_type(self, ctx:ZCodeParser.Statement_typeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement_type.
    def exitStatement_type(self, ctx:ZCodeParser.Statement_typeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement.
    def enterStatement(self, ctx:ZCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement.
    def exitStatement(self, ctx:ZCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_assignment.
    def enterStmt_assignment(self, ctx:ZCodeParser.Stmt_assignmentContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_assignment.
    def exitStmt_assignment(self, ctx:ZCodeParser.Stmt_assignmentContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignment_lhs.
    def enterAssignment_lhs(self, ctx:ZCodeParser.Assignment_lhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignment_lhs.
    def exitAssignment_lhs(self, ctx:ZCodeParser.Assignment_lhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_statement.
    def enterIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_statement.
    def exitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_statement.
    def enterElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_statement.
    def exitElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#else_statement.
    def enterElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#else_statement.
    def exitElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_if.
    def enterStmt_if(self, ctx:ZCodeParser.Stmt_ifContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_if.
    def exitStmt_if(self, ctx:ZCodeParser.Stmt_ifContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifLst.
    def enterElifLst(self, ctx:ZCodeParser.ElifLstContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifLst.
    def exitElifLst(self, ctx:ZCodeParser.ElifLstContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_for.
    def enterStmt_for(self, ctx:ZCodeParser.Stmt_forContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_for.
    def exitStmt_for(self, ctx:ZCodeParser.Stmt_forContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_break.
    def enterStmt_break(self, ctx:ZCodeParser.Stmt_breakContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_break.
    def exitStmt_break(self, ctx:ZCodeParser.Stmt_breakContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_continue.
    def enterStmt_continue(self, ctx:ZCodeParser.Stmt_continueContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_continue.
    def exitStmt_continue(self, ctx:ZCodeParser.Stmt_continueContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_return.
    def enterStmt_return(self, ctx:ZCodeParser.Stmt_returnContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_return.
    def exitStmt_return(self, ctx:ZCodeParser.Stmt_returnContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_func_call.
    def enterStmt_func_call(self, ctx:ZCodeParser.Stmt_func_callContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_func_call.
    def exitStmt_func_call(self, ctx:ZCodeParser.Stmt_func_callContext):
        pass


    # Enter a parse tree produced by ZCodeParser#argLst.
    def enterArgLst(self, ctx:ZCodeParser.ArgLstContext):
        pass

    # Exit a parse tree produced by ZCodeParser#argLst.
    def exitArgLst(self, ctx:ZCodeParser.ArgLstContext):
        pass


    # Enter a parse tree produced by ZCodeParser#argLstTail.
    def enterArgLstTail(self, ctx:ZCodeParser.ArgLstTailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#argLstTail.
    def exitArgLstTail(self, ctx:ZCodeParser.ArgLstTailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_block.
    def enterStmt_block(self, ctx:ZCodeParser.Stmt_blockContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_block.
    def exitStmt_block(self, ctx:ZCodeParser.Stmt_blockContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statementLst.
    def enterStatementLst(self, ctx:ZCodeParser.StatementLstContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statementLst.
    def exitStatementLst(self, ctx:ZCodeParser.StatementLstContext):
        pass



del ZCodeParser