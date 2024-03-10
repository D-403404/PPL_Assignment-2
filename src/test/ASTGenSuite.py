import unittest
from TestUtils import TestAST
from AST import *

# from main.zcode.utils.AST import *

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
    
    def test_simple_program_3(self):
        input = """func main() return 1
"""
        expect = "Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program_4(self):
        input = """func inc(number a) return a + 1
func main() begin
var a <- 1
inc(a)
writeNumber(a)
end
"""
        expect = "Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"
        self.assertTrue(TestAST.test(input, expect, 303))

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
    
    def test_simple_program_6(self):
        input = """func main() begin
if (1) writeString("1")
elif (2) if(3) writeString("1")
elif (4) writeString("1")
else writeString("1")
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"
        # expect = str(Program([FuncDecl(Id('main'), [], Block([If(NumberLiteral(1.0), CallStmt(Id('writeString'), [StringLiteral(1)]), [(NumberLiteral(2.0), If(NumberLiteral(3.0), CallStmt(Id('writeString'), [StringLiteral(1)]), [(NumberLiteral(4.0), CallStmt(Id('writeString'), [StringLiteral(1)]))], CallStmt(Id('writeString'), [StringLiteral(1)])))], None)]))]))
        # print(expect==expect1) # True
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_simple_program_7(self):
        input = """
func main()
begin
    var i <- 0
    number j <- 0
    for i until i <= 10 by 2
    begin
        for j until j <= 20 by 4
            writeNumber(i*j)
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 306))
    
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

#===============================================================
        
    def test_1(self):
        input = """
func main ()
begin
    if (1)
        b()
    elif (2)
        if (3)
            c()
        elif (4)
            d()
        else
            e()
end
"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([If(NumberLiteral(1.), CallStmt(Id('b'), []), [(NumberLiteral(2.), If(NumberLiteral(3.), CallStmt(Id('c'), []), [(NumberLiteral(4.), CallStmt(Id('d'), []))],CallStmt(Id('e'), [])))],None)]))]))
        self.assertTrue(TestAST.test(input, expect, 2001))
    
    def test_2(self):
        input = """
func main ()
begin
    if (1)
        b()
    elif (2)
        c()
    else d()
end
"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([If(NumberLiteral(1.), CallStmt(Id('b'), []), [(NumberLiteral(2.), CallStmt(Id('c'), []))], CallStmt(Id('d'), []))]))]))
        self.assertTrue(TestAST.test(input, expect, 2002))
    
    def test_3(self):
        input = """
func main ()
begin
    if (1)
        b()
    else d()
end
"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([If(NumberLiteral(1.), CallStmt(Id('b'), []), [], CallStmt(Id('d'), []))]))]))
        self.assertTrue(TestAST.test(input, expect, 2003))
    
    def test_4(self):
        '''test_1001 ParserSuite'''
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            ## comment lollll
            func main()             ## comment\\r lollll
                begin
                    var num1 <- readNumber()
                    var num2 <- readNumber()

                    if (areDivisors(num1, num2)) printString("Yes")
                    else printString("No")
                end
                ## comment lollll \n"""
        expect = str(Program([
            FuncDecl(Id('areDivisors'), 
                [VarDecl(Id('num1'),NumberType()), 
                    VarDecl(Id('num2'), NumberType())], 
                Return(BinaryOp('or', BinaryOp('=', BinaryOp('%', Id('num1'), Id('num2')), NumberLiteral(0.)), BinaryOp('=', BinaryOp('%', Id('num2'), Id('num1')), NumberLiteral(0.))))), 
            FuncDecl(Id('main'), [], 
                Block([
                    VarDecl(Id('num1'), None, 'var', CallExpr(Id('readNumber'), [])), 
                    VarDecl(Id('num2'), None, 'var', CallExpr(Id('readNumber'), [])), 
                    If(CallExpr(Id('areDivisors'), [Id('num1'), Id('num2')]), 
                        CallStmt(Id('printString'), [StringLiteral('Yes')]), 
                        [], 
                        CallStmt(Id('printString'), [StringLiteral('No')]))]))]))
        self.assertTrue(TestAST.test(input, expect, 2004))
    
    def test_5(self):
        '''test_1002 ParserSuite'''
        input = """
            func isPrime(number x)

            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end

            func isPrime(number x)
                begin
                    if (x <= 1) return false
                    var i <- 2
                    for i until i > x / 2 by 1
                    begin
                        if (x % i = 0) return false
                    end
                return true
                end
                """
        expect = str(Program([
            FuncDecl(Id('isPrime'), [VarDecl(Id('x'),NumberType())]), 
            FuncDecl(Id('main'), [], 
                Block([
                    VarDecl(Id('x'), NumberType(), None, CallExpr(Id('readNumber'), [])), 
                    If(CallExpr(Id('isPrime'), [Id('x')]), 
                        CallStmt(Id('printString'), [StringLiteral('Yes')]), 
                        [], 
                        CallStmt(Id('printString'), [StringLiteral('No')]))])), 
            FuncDecl(Id('isPrime'), [VarDecl(Id('x'),NumberType())],
                Block([
                    If(BinaryOp('<=', Id('x'), NumberLiteral(1.)), Return(BooleanLiteral(False)), [], None), 
                    VarDecl(Id('i'), None, 'var', NumberLiteral(2.)), 
                    For(Id('i'), 
                        BinaryOp('>', Id('i'), BinaryOp('/', Id('x'), NumberLiteral(2.))), 
                        NumberLiteral(1.), 
                        Block([If(BinaryOp('=', BinaryOp('%', Id('x'), Id('i')), NumberLiteral(0.)), Return(BooleanLiteral(False)), [], None)])),
                    Return(BooleanLiteral(True))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 2005))
    
    def test_6(self):
        '''test_1006 ParserSuite'''
        input = """string s <- writeString("Hello this is a '"test'"") \\n"""
        expect = str(Program([VarDecl(Id('s'), StringType(), None, CallExpr(Id('writeString'), [StringLiteral('Hello this is a \'"test\'"')]))]))
        self.assertTrue(TestAST.test(input, expect, 2006))
    
    def test_7(self):
        '''test_1007 ParserSuite'''
        input = """func foo(number arr[1,2,3])
        """
        expect = str(Program([FuncDecl(Id('foo'), [VarDecl(Id('arr'), ArrayType([1., 2., 3.], NumberType()), None, None)], None)]))
        self.assertTrue(TestAST.test(input, expect, 2007))
    
    def test_8(self):
        '''test_1012 ParserSuite'''
        input = """
func foo()
    begin
        if (a < b) if (c < d) bool e
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([If(BinaryOp('<', Id('a'), Id('b')), If(BinaryOp('<', Id('c'), Id('d')), VarDecl(Id('e'), BoolType(), None, None), [], None), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 2008))
    
    def test_9(self):
        '''test_1015 ParserSuite'''
        input = """
func foo(number a[5], string b)
begin
var i <- 0
for i until i >= 5 by 1
begin
a[i] <- i * i + 5
end
return -1
end
        """
        expect = str(Program([FuncDecl(Id('foo'), [VarDecl(Id('a'), ArrayType([5.], NumberType()), None, None), VarDecl(Id('b'), StringType(), None, None)], 
                        Block([
                            VarDecl(Id('i'), None, 'var', NumberLiteral(0.)),
                            For(Id('i'), BinaryOp('>=', Id('i'), NumberLiteral(5.)), NumberLiteral(1.), Block([Assign(ArrayCell(Id('a'), [Id('i')]), BinaryOp('+', BinaryOp('*', Id('i'), Id('i')), NumberLiteral(5.)))])),
                            Return(UnaryOp('-', NumberLiteral(1.)))]))]))
        self.assertTrue(TestAST.test(input, expect, 2009))
    
    def test_10(self):
        input = """
var a <- 23.51e-30
"""
        expect = str(Program([VarDecl(Id('a'), None, 'var', NumberLiteral(23.51e-30))]))
        self.assertTrue(TestAST.test(input, expect, 2010))
    
    def test_11(self):
        input = """

string array[1,2,3,1] <- [3,"abcd",5., true, True, False, false]

"""
        expect = str(Program([VarDecl(Id('array'), ArrayType([1., 2., 3., 1.], StringType()), None, ArrayLiteral([NumberLiteral(3.), StringLiteral('abcd'), NumberLiteral(5.), BooleanLiteral(True), Id('True'), Id('False'), BooleanLiteral(False)]))]))
        self.assertTrue(TestAST.test(input, expect, 2011))
    
    def test_12(self):
        input = """
func foo(number a[2], number __aaaaa__, string b[1,2,3], bool arr[3.3,4e4,5.,0.5])
    begin
        if (f==2)
            begin
                if (a<2) continue
                if (b>3) continue
                if (c<=4) continue
                if (d>=5) continue
                elif (d==5 and (d!=5)) break
                elif (d!=5 and ((d==__) and d==5)) break
                elif ((c!="") and (c==0)) return _bool(true)
                elif ((c==true and (c=4)) and 4=c) return
                ##else goo(1,2,3)
                elif (true) begin\nend\n
                else begin\nend\n
            end
        elif (false) begin\nend\n
    end
"""
        expect = str(Program([
                    FuncDecl(Id('foo'), [
                            VarDecl(Id('a'), ArrayType([2.], NumberType()), None, None), 
                            VarDecl(Id('__aaaaa__'), NumberType(), None, None), 
                            VarDecl(Id('b'), ArrayType([1., 2., 3.], StringType()), None, None), 
                            VarDecl(Id('arr'), ArrayType([3.3, 4e4, 5., .5], BoolType()), None, None)], 
                        Block([If(BinaryOp('==', Id('f'), NumberLiteral(2.)), 
                            Block([
                                If(BinaryOp('<', Id('a'), NumberLiteral(2.)), Continue(), [], None), 
                                If(BinaryOp('>', Id('b'), NumberLiteral(3.)), Continue(), [], None), 
                                If(BinaryOp('<=', Id('c'), NumberLiteral(4.)), Continue(), [], None), 
                                If(BinaryOp('>=', Id('d'), NumberLiteral(5.)), Continue(), [
                                    (BinaryOp('==', Id('d'), BinaryOp('and', NumberLiteral(5.), BinaryOp('!=', Id('d'), NumberLiteral(5.)))), Break()), 
                                    (BinaryOp('!=', Id('d'), BinaryOp('and', NumberLiteral(5.), BinaryOp('==', BinaryOp('and', BinaryOp('==', Id('d'), Id('__')), Id('d')), NumberLiteral(5.)))), Break()), 
                                    (BinaryOp('and', BinaryOp('!=', Id('c'), StringLiteral('')), BinaryOp('==', Id('c'), NumberLiteral(0.))), Return(CallExpr(Id('_bool'), [BooleanLiteral(True)]))), 
                                    (BinaryOp('=', BinaryOp('and', BinaryOp('==', Id('c'), BinaryOp('and', BooleanLiteral(True), BinaryOp('=', Id('c'), NumberLiteral(4.)))), NumberLiteral(4.)), Id('c')), Return(None)), 
                                    (BooleanLiteral(True), Block([]))
                                    ], Block([]))]), 
                            [(BooleanLiteral(False), Block([]))], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 2012))
    
    def test_13(self):
        input = """
func foo(number a[2], number __aaaaa__, string b[1,2,3], bool arr[3.3,4e4,5.,0.5])
    begin
        if (f==2)
            begin
                if (a<2) continue
                if (b>3) continue
                if (c<=4) 
                    if (d>=5) continue
                    elif (d==5 and (d!=5)) break
                    elif (d!=5 and ((d==__) and d==5)) break
                    elif ((c!="") and (c==0)) return _bool(true)
                    elif ((c==true and (c=4)) and 4=c) return
                    else goo(1,2,3)
                elif (true) begin\nend\n
                else begin\nend\n
            end
        elif (false) begin\nend\n
    end
"""
        expect = str(Program([
                    FuncDecl(Id('foo'), [
                            VarDecl(Id('a'), ArrayType([2.], NumberType()), None, None), 
                            VarDecl(Id('__aaaaa__'), NumberType(), None, None), 
                            VarDecl(Id('b'), ArrayType([1., 2., 3.], StringType()), None, None), 
                            VarDecl(Id('arr'), ArrayType([3.3, 4e4, 5., .5], BoolType()), None, None)], 
                        Block([If(BinaryOp('==', Id('f'), NumberLiteral(2.)), 
                            Block([
                                If(BinaryOp('<', Id('a'), NumberLiteral(2.)), Continue(), [], None), 
                                If(BinaryOp('>', Id('b'), NumberLiteral(3.)), Continue(), [], None), 
                                If(BinaryOp('<=', Id('c'), NumberLiteral(4.)), 
                                    If(BinaryOp('>=', Id('d'), NumberLiteral(5.)), Continue(), [
                                        (BinaryOp('==', Id('d'), BinaryOp('and', NumberLiteral(5.), BinaryOp('!=', Id('d'), NumberLiteral(5.)))), Break()), 
                                        (BinaryOp('!=', Id('d'), BinaryOp('and', NumberLiteral(5.), BinaryOp('==', BinaryOp('and', BinaryOp('==', Id('d'), Id('__')), Id('d')), NumberLiteral(5.)))), Break()), 
                                        (BinaryOp('and', BinaryOp('!=', Id('c'), StringLiteral('')), BinaryOp('==', Id('c'), NumberLiteral(0.))), Return(CallExpr(Id('_bool'), [BooleanLiteral(True)]))), 
                                        (BinaryOp('=', BinaryOp('and', BinaryOp('==', Id('c'), BinaryOp('and', BooleanLiteral(True), BinaryOp('=', Id('c'), NumberLiteral(4.)))), NumberLiteral(4.)), Id('c')), Return(None))
                                        ], 
                                        CallStmt(Id('goo'), [NumberLiteral(1.), NumberLiteral(2.), NumberLiteral(3.)])), 
                                [(BooleanLiteral(True), Block([]))], Block([]))]), 
                        [(BooleanLiteral(False), Block([]))], None)]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 2013))
    
    def test_14(self):
        '''test_1016 ParserSuite'''
        input = """
        var a <- [abc,xyz]
        """
        expect = str(Program([VarDecl(Id('a'), None, 'var', ArrayLiteral([Id('abc'), Id('xyz')]))]))
        self.assertTrue(TestAST.test(input, expect, 2014))
    
    def test_15(self):
        '''test_1022 ParserSuite'''
        input = """##number a\nnumber a\n##\\n var b\n"""
        expect = str(Program([VarDecl(Id('a'), NumberType(), None, None)]))
        self.assertTrue(TestAST.test(input, expect, 2015))
    
    def test_16(self):
        '''test_1028 ParserSuite'''
        input = """
            dynamic engineergaming123<-e2xyz
            func foo() begin\nend
"""
        expect = str(Program([VarDecl(Id('engineergaming123'), None, 'dynamic', Id('e2xyz')), FuncDecl(Id('foo'), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 2016))
    
    def test_17(self):
        '''test_1029 ParserSuite'''
        input = """
            var engineergaming123<-e2xyz
            func foo() begin\n\n\n\n\r\n\r\r\rend
"""
        expect = str(Program([VarDecl(Id('engineergaming123'), None, 'var', Id('e2xyz')), FuncDecl(Id('foo'), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 2017))
    
    def test_18(self):
        '''test_1038 ParserSuite'''
        input = """
func main()
        begin   \\n  var i <- 0\nfoo()[3 + foo(2)] <- a[b[2, 3]] + 4
    end\\n"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([VarDecl(Id('i'), None, 'var', NumberLiteral(0.)), Assign(ArrayCell(CallExpr(Id('foo'), []), [BinaryOp('+', NumberLiteral(3.), CallExpr(Id('foo'), [NumberLiteral(2.)]))]), BinaryOp('+', ArrayCell(Id('a'), [ArrayCell(Id('b'), [NumberLiteral(2.), NumberLiteral(3.)])]), NumberLiteral(4.)))]))]))
        self.assertTrue(TestAST.test(input, expect, 2018))
    
    def test_19(self):
        '''test_1039 ParserSuite'''
        input = """
func main()      \n  """
        expect = str(Program([FuncDecl(Id('main'), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 2019))
    
    def test_20(self):
        '''test_1049 ParserSuite'''
        input = """
number a <- "kdoqqw123" + 42E24
bool b <- true and false or not not s[20]
string c <- [r,t,x[3]]
var d <- [3,4,[5,6,7],[8,9,0]] + [[23]]
dynamic e
        """
        expect = str(Program([
                    VarDecl(Id('a'), NumberType(), None, BinaryOp('+', StringLiteral('kdoqqw123'), NumberLiteral(42E24))), 
                    VarDecl(Id('b'), BoolType(), None, BinaryOp('or', BinaryOp('and', BooleanLiteral(True), BooleanLiteral(False)), UnaryOp('not', UnaryOp('not', ArrayCell(Id('s'), [NumberLiteral(20.)]))))), 
                    VarDecl(Id('c'), StringType(), None, ArrayLiteral([Id('r'), Id('t'), ArrayCell(Id('x'), [NumberLiteral(3.)])])), 
                    VarDecl(Id('d'), None, 'var', BinaryOp('+', ArrayLiteral([NumberLiteral(3.), NumberLiteral(4.), ArrayLiteral([NumberLiteral(5.), NumberLiteral(6.), NumberLiteral(7.)]), ArrayLiteral([NumberLiteral(8.), NumberLiteral(9.), NumberLiteral(0.)])]), ArrayLiteral([ArrayLiteral([NumberLiteral(23.)])]))), 
                    VarDecl(Id('e'), None, 'dynamic', None)
                    ]))
        self.assertTrue(TestAST.test(input, expect, 2020))
    
    def test_21(self):
        '''test_1051 ParserSuite'''
        input = """
number a <- "kdoqqw123" + 42E24
bool b <- true and false or not (not s[20] and 7E3)
string c <- ([r,t,x[3]])
dynamic e <- abc
var d <- [3,4,[5,6,7],[8,9,0]] + [foo[23],_foo(str)[foo()]]
        """
        expect = str(Program([
                    VarDecl(Id('a'), NumberType(), None, BinaryOp('+', StringLiteral('kdoqqw123'), NumberLiteral(42E24))), 
                    VarDecl(Id('b'), BoolType(), None, BinaryOp('or', BinaryOp('and', BooleanLiteral(True), BooleanLiteral(False)), UnaryOp('not', BinaryOp('and', UnaryOp('not', ArrayCell(Id('s'), [NumberLiteral(20.)])), NumberLiteral(7E3))))), 
                    VarDecl(Id('c'), StringType(), None, ArrayLiteral([Id('r'), Id('t'), ArrayCell(Id('x'), [NumberLiteral(3.)])])), 
                    VarDecl(Id('e'), None, 'dynamic', Id('abc')), 
                    VarDecl(Id('d'), None, 'var', BinaryOp('+', ArrayLiteral([NumberLiteral(3.), NumberLiteral(4.), ArrayLiteral([NumberLiteral(5.), NumberLiteral(6.), NumberLiteral(7.)]), ArrayLiteral([NumberLiteral(8.), NumberLiteral(9.), NumberLiteral(0.)])]), ArrayLiteral([ArrayCell(Id('foo'), [NumberLiteral(23.)]), ArrayCell(CallExpr(Id('_foo'), [Id('str')]), [CallExpr(Id('foo'), [])])])))
                    ]))
        self.assertTrue(TestAST.test(input, expect, 2021))
    
    def test_22(self):
        '''test_1053 ParserSuite'''
        input = """
func foo()
    begin
        if (not x)
            return ---(--1)
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([If(UnaryOp('not', Id('x')), Return(UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', NumberLiteral(1.))))))))]))]))
        self.assertTrue(TestAST.test(input, expect, 2022))
    
    def test_23(self):
        '''test_1054 ParserSuite'''
        input = """
func foo()
    begin
        if ((x <= (y > z) ... "abc") ... ["xyz"...foo()])
            return ---(--1)
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([If(BinaryOp('...', BinaryOp('...', BinaryOp('<=', Id('x'), BinaryOp('>', Id('y'), Id('z'))), StringLiteral('abc')), ArrayLiteral([BinaryOp('...', StringLiteral('xyz'), CallExpr(Id('foo'), []))])), Return(UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', NumberLiteral(1.))))))))]))]))
        self.assertTrue(TestAST.test(input, expect, 2023))
    
    def test_24(self):
        '''test_1055 ParserSuite'''
        input = """
func foo()
    begin
        if ((x <= (y > z) ... "abc") ... ["xyz"...foo([[1,23,4],[2,"abc'"abc"]])])
            return ---(--1)
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([If(BinaryOp('...', BinaryOp('...', BinaryOp('<=', Id('x'), BinaryOp('>', Id('y'), Id('z'))), StringLiteral('abc')), ArrayLiteral([BinaryOp('...', StringLiteral('xyz'), CallExpr(Id('foo'), [ArrayLiteral([ArrayLiteral([NumberLiteral(1.), NumberLiteral(23.), NumberLiteral(4.)]), ArrayLiteral([NumberLiteral(2.), StringLiteral('abc\'"abc')])])]))])), Return(UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', NumberLiteral(1.))))))))]))]))
        self.assertTrue(TestAST.test(input, expect, 2024))
    
    def test_25(self):
        '''test_1060 ParserSuite'''
        input = """
func foo()
    begin
        aPI <- 3.14
        value <- x%[foo(5)]
        l[3] <- value * aPi
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([
            Assign(Id('aPI'), NumberLiteral(3.14)), 
            Assign(Id('value'), BinaryOp('%', Id('x'), ArrayLiteral([CallExpr(Id('foo'), [NumberLiteral(5.)])]))), 
            Assign(ArrayCell(Id('l'), [NumberLiteral(3.)]), BinaryOp('*', Id('value'), Id('aPi'))), 
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 2025))
    
    def test_26(self):
        input = """
string a[3] <- 1 * (2 + 3)
bool b[4.3,3e4] <- false
        """
        expect = str(Program([VarDecl(Id('a'), ArrayType([3.], StringType()), None, BinaryOp('*', NumberLiteral(1.), BinaryOp('+', NumberLiteral(2.), NumberLiteral(3.)))), VarDecl(Id('b'), ArrayType([4.3, 3e4], BoolType()), None, BooleanLiteral(False))]))
        self.assertTrue(TestAST.test(input, expect, 2026))
    
    def test_27(self):
        '''test_1067 ParserSuite'''
        input = """
func foo()
begin
var i <- 0
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([VarDecl(Id('i'), None, 'var', NumberLiteral(0.)), For(Id('i'), BinaryOp('>=', Id('i'), NumberLiteral(10.)), NumberLiteral(1.), CallStmt(Id('writeNumbe'), [Id('i')]))]))]))
        self.assertTrue(TestAST.test(input, expect, 2027))
    
    def test_28(self):
        '''test_1069 ParserSuite'''
        input = """
func foo()
begin
number i[1,2,3] <- [[1,2],3]
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([VarDecl(Id('i'), ArrayType([1., 2., 3.], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.), NumberLiteral(2.)]), NumberLiteral(3.)])), For(Id('i'), BinaryOp('>=', Id('i'), NumberLiteral(10.)), NumberLiteral(1.), CallStmt(Id('writeNumbe'), [Id('i')]))]))]))
        self.assertTrue(TestAST.test(input, expect, 2028))
    
    def test_29(self):
        '''test_1074 ParserSuite'''
        input = """
func foo()
    begin
        number r
        number s
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([
            VarDecl(Id('r'), NumberType(), None, None), 
            VarDecl(Id('s'), NumberType(), None, None), 
            Assign(Id('r'), NumberLiteral(2.0)), 
            VarDecl(Id('a'), ArrayType([5.], NumberType()), None, None), 
            VarDecl(Id('b'), ArrayType([5.], NumberType()), None, None), 
            Assign(Id('s'), BinaryOp('*', BinaryOp('*', Id('r'), Id('r')), NumberLiteral(3.14))), 
            Assign(ArrayCell(Id('a'), [NumberLiteral(0.)]), Id('s'))
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 2029))
    
    def test_30(self):
        '''test_1079 ParserSuite'''
        input = """
func foo()
    begin
        number _##"abc"^^^\n
        number s
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([
            VarDecl(Id('_'), NumberType(), None, None), 
            VarDecl(Id('s'), NumberType(), None, None), 
            Assign(Id('r'), NumberLiteral(2.0)), 
            VarDecl(Id('a'), ArrayType([5.], NumberType()), None, None), 
            VarDecl(Id('b'), ArrayType([5.], NumberType()), None, None), 
            Assign(Id('s'), BinaryOp('*', BinaryOp('*', Id('r'), Id('r')), NumberLiteral(3.14))), 
            Assign(ArrayCell(Id('a'), [NumberLiteral(0.)]), Id('s'))
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 2030))
    
    def test_31(self):
        '''test_1081 ParserSuite'''
        input = """
dynamic r <- a - b * a/b
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('-', Id('a'), BinaryOp('/', BinaryOp('*', Id('b'), Id('a')), Id('b'))))]))
        self.assertTrue(TestAST.test(input, expect, 2031))
    
    def test_32(self):
        '''test_1082 ParserSuite'''
        input = """
dynamic r <- (a - (b * a/b))
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('-', Id('a'), BinaryOp('/', BinaryOp('*', Id('b'), Id('a')), Id('b'))))]))
        self.assertTrue(TestAST.test(input, expect, 2032))
    
    def test_33(self):
        '''test_1083 ParserSuite'''
        input = """
dynamic r <- ((a - b) * (a/b))...(a%b) + (a - (b + c) * 3)
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('...', BinaryOp('*', BinaryOp('-', Id('a'), Id('b')), BinaryOp('/', Id('a'), Id('b'))), BinaryOp('+', BinaryOp('%', Id('a'), Id('b')), BinaryOp('-', Id('a'), BinaryOp('*', BinaryOp('+', Id('b'), Id('c')), NumberLiteral(3.))))))]))
        self.assertTrue(TestAST.test(input, expect, 2033))
    
    def test_34(self):
        '''test_1084 ParserSuite'''
        input = """
dynamic r <- not((a - b) * (a/b))...(a%b) == (a or (b + c) and 3)
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('...', UnaryOp('not', BinaryOp('*', BinaryOp('-', Id('a'), Id('b')), BinaryOp('/', Id('a'), Id('b')))), BinaryOp('==', BinaryOp('%', Id('a'), Id('b')), BinaryOp('and', BinaryOp('or', Id('a'), BinaryOp('+', Id('b'), Id('c'))), NumberLiteral(3.)))))]))
        self.assertTrue(TestAST.test(input, expect, 2034))
    
    def test_35(self):
        '''test_1085 ParserSuite'''
        input = """
dynamic r <- not((a - b) * (a/b))...(a%b) == (a ... (b <= c) and 3 and a[(a+(b/c)),foo([a,b,c])])
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('...', UnaryOp('not', BinaryOp('*', BinaryOp('-', Id('a'), Id('b')), BinaryOp('/', Id('a'), Id('b')))), BinaryOp('==', BinaryOp('%', Id('a'), Id('b')), BinaryOp('...', Id('a'), BinaryOp('and', BinaryOp('and', BinaryOp('<=', Id('b'), Id('c')), NumberLiteral(3.)), ArrayCell(Id('a'), [BinaryOp('+', Id('a'), BinaryOp('/', Id('b'), Id('c'))), CallExpr(Id('foo'), [ArrayLiteral([Id('a'), Id('b'), Id('c')])])]))))))]))
        self.assertTrue(TestAST.test(input, expect, 2035))
    
    def test_36(self):
        '''test_1090 ParserSuite'''
        input = """
dynamic r <- not(((-a - -b) * (a/b)) = ((((-a%b) == (a ... (b <= c) and 3 >= a[(a != (b/c)),foo([a,b,c])]))) < (a > [b,c()[d[e]...((a >= b)...-c)]])))
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', 
                    UnaryOp('not', 
                        BinaryOp('=', 
                            BinaryOp('*', 
                                BinaryOp('-', UnaryOp('-', Id('a')), UnaryOp('-', Id('b'))), 
                                BinaryOp('/', Id('a'), Id('b'))), 
                            BinaryOp('<', 
                                BinaryOp('==', 
                                    BinaryOp('%', UnaryOp('-', Id('a')), Id('b')), 
                                    BinaryOp('...', Id('a'), 
                                        BinaryOp('>=', 
                                            BinaryOp('and', BinaryOp('<=', Id('b'), Id('c')), NumberLiteral(3.)), 
                                            ArrayCell(Id('a'), [
                                                BinaryOp('!=', Id('a'), BinaryOp('/', Id('b'), Id('c'))), 
                                                CallExpr(Id('foo'), [ArrayLiteral([Id('a'), Id('b'), Id('c')])])])))), 
                                BinaryOp('>', Id('a'), 
                                    ArrayLiteral([
                                        Id('b'), 
                                        ArrayCell(CallExpr(Id('c'), []), [BinaryOp('...', ArrayCell(Id('d'), [Id('e')]), BinaryOp('...', BinaryOp('>=', Id('a'), Id('b')), UnaryOp('-', Id('c'))))])])))), 
                    ))]))
        self.assertTrue(TestAST.test(input, expect, 2036))
    
    def test_37(self):
        '''test_1093 ParserSuite'''
        input = """func main()\nbegin\nend\n"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 2037))
    
    def test_38(self):
        '''test_1095 ParserSuite'''
        input = """
func goo (number a, number b)
    return 1 - foo(1, a, b)
"""
        expect = str(Program([FuncDecl(Id('goo'), [VarDecl(Id('a'), NumberType()), VarDecl(Id('b'), NumberType())], Return(BinaryOp('-', NumberLiteral(1.), CallExpr(Id('foo'), [NumberLiteral(1.), Id('a'), Id('b')]))))]))
        self.assertTrue(TestAST.test(input, expect, 2038))
    
    def test_39(self):
        '''test_1098 ParserSuite'''
        input = """
number a
number b
number c

func foo(number a, string c, bool d)
    begin
        dynamic e
        e <- a + 4
        c <- a * d / 2.0
        return c + 1
    end

func goo (number a, number b)
    return foo(1, a, b)
"""
        expect = str(Program([
                    VarDecl(Id('a'), NumberType(), None, None), 
                    VarDecl(Id('b'), NumberType(), None, None), 
                    VarDecl(Id('c'), NumberType(), None, None), 
                    FuncDecl(Id('foo'), [VarDecl(Id('a'), NumberType()), VarDecl(Id('c'), StringType()), VarDecl(Id('d'), BoolType())], Block([
                        VarDecl(Id('e'), None, 'dynamic', None), 
                        Assign(Id('e'), BinaryOp('+', Id('a'), NumberLiteral(4.))), 
                        Assign(Id('c'), BinaryOp('/', BinaryOp('*', Id('a'), Id('d')), NumberLiteral(2.))), 
                        Return(BinaryOp('+', Id('c'), NumberLiteral(1.)))
                    ])), 
                    FuncDecl(Id('goo'), [VarDecl(Id('a'), NumberType()), VarDecl(Id('b'), NumberType())], Return(CallExpr(Id('foo'), [NumberLiteral(1.), Id('a'), Id('b')])))]))
        self.assertTrue(TestAST.test(input, expect, 2039))