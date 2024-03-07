import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
    
    def test_simple_program_2(self):
        input = """var str <- "Hello world!"
"""
        expect = str(Program([VarDecl(Id("str"), None, "var", StringLiteral("Hello world!"))]))
        self.assertTrue(TestAST.test(input, expect, 301))
    
    def test_simple_program_5(self):
        input = """func main() begin
number a
if (5 < 2) a <- 1
elif (not true) a <- 2
elif ("h" == "6") a <- 3
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 304))
    
    def test_simple_program_8(self):
        input = """
number a <- 100

func sum(number n)
begin
    if (n = 0) return 0
    return n + sum(n - 1)
end

func main()
begin
    writeNumber(sum(a))
end
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"
        self.assertTrue(TestAST.test(input, expect, 307))
