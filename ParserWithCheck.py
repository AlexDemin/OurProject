import sly
import math
import sympy
from sympy import*
from numpy import random


class VisualMathLexer(sly.Lexer):
    tokens = { NUMBER, NAME, E, PI, SIN, COS, TG, TAN, CTG, CTAN, COT,
               ARCSIN, ASIN, ARCCOS, ACOS, ARCTG, ARCTAN, ATG, ATAN, ARCCTG, ACTG, ACTAN, ARCCOT, 
               LOG, LG, LN, SH, CH, SQRT}

    literals = { '+', '-', '*', '/', '^', '(', ')', '{', '}', '[', ']', ','}

    ignore = ' \r\t\n'

    ignore_comment = r'\#.*'

    E = r'\\?e'
    PI = r'\\?pi'
    SIN = 'sin'
    COS = 'cos'
    TG = 'tg'
    TAN = 'tan'
    CTG = 'ctg'
    CTAN = 'ctan'
    COT = 'cot'
    ARCSIN = 'arcsin'
    ASIN = 'asin'
    ARCCOS = 'arccos'
    ACOS = 'acos'
    ARCTG = 'arctg'
    ARCTAN = 'arctan'
    ATG = 'atg'
    ATAN = 'atan'
    ARCCTG = 'arcctg'
    ACTG = 'actg'
    ACTAN = 'actan'
    ARCCOT = 'arccot'
    SH = 'sh'
    CH = 'ch'
    LOG = 'log'
    LG = 'lg'
    LN = 'ln'
    SQRT = 'sqrt'


    @_(r'[0-9]+\.[0-9]+', r'\d+')
    def NUMBER(self, t):
        t.value = float(t.value)
        return t

    @_(r'[a-df-z_]')
    def NAME(self, t):
        t.value = ord(t.value) #(int)(t.value)
        return t


class ASTNode(object):
    def compute(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class VarNode(ASTNode):
    def __init__(self, n):
        self.n = n

    def compute(self):
        return 0

    def __str__(self):
        return chr(self.n)
    
    def str2(self):
        return chr(self.n)


class NumNode(ASTNode):
    def __init__(self, n):
        self.n = n

    def compute(self):
        return self.n

    def __str__(self):
        return str(self.n)

    def str2(self):
        return str(self.n)

class MinusNode(ASTNode):
    def __init__(self, n):
        self.n = n

    def compute(self):
        return (-1) * self.n.compute()

    def __str__(self):
        return "-" + str(self.n)

    def str2(self):
        return "(-" + self.n.str2() + ")"

class ENode(ASTNode):
    def __init__(self):
        self.n = math.e

    def compute(self):
        return math.e

    def __str__(self):
        return "e"

    def str2(self):
        return "E"

class PiNode(ASTNode):
    def __init__(self):
        self.n = math.pi

    def compute(self):
        return math.pi

    def __str__(self):
        return "pi"

    def str2(self):
        return "pi"

class AddNode(ASTNode):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def compute(self):
        return self.l.compute() + self.r.compute()

    def __str__(self):
        return f'({self.l})+({self.r})'

    def str2(self):
        return "(" + self.l.str2() + "+" + self.r.str2() + ")"

class SubNode(ASTNode):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def compute(self):
        return self.l.compute() - self.r.compute()

    def __str__(self):
        return f'({self.l})-({self.r})'

    def str2(self):
        return "(" + self.l.str2() + "-" + self.r.str2() + ")"


class MultNode(ASTNode):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def compute(self):
        return self.l.compute() * self.r.compute()

    def __str__(self):
        return f'({self.l})*({self.r})'

    def str2(self):
        return "(" + self.l.str2() + "*" + self.r.str2() + ")"


class DivNode(ASTNode):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def compute(self):
        return self.l.compute() / self.r.compute()

    def __str__(self):
        return f'({self.l})/({self.r})'

    def str2(self):
        return "(" + self.l.str2() + "/" + self.r.str2() + ")"


class PowNode(ASTNode):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def compute(self):
        return math.pow(self.l.compute(), self.r.compute())

    def __str__(self):
        return f'({self.l})^({self.r})'

    def str2(self):
        return "(" + self.l.str2() + "**" + self.r.str2() + ")"


class SqrtNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.sqrt(self.l.compute())

    def __str__(self):
        return f'sqrt({self.l})'

    def str2(self):
        return "(" + "sqrt(" + self.l.str2() + ")" + ")"


class SinNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.sin(self.l.compute())

    def __str__(self):
        return f'sin({self.l})'

    def str2(self):
        return "(" + "sin(" + self.l.str2() + ")" + ")"


class CosNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.cos(self.l.compute())

    def __str__(self):
        return f'cos({self.l})'

    def str2(self):
        return "(" + "cos(" + self.l.str2() + ")" + ")"


class TgNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.tan(self.l.compute())

    def __str__(self):
        return f'tg({self.l})'

    def str2(self):
        return "(" + "tan(" + self.l.str2() + ")" + ")"


class CtgNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.tan(math.pi / 2 - self.l.compute())

    def __str__(self):
        return f'ctg({self.l})'

    def str2(self):
        return "(" + "cot(" + self.l.str2() + ")" + ")"


class ArcsinNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.asin(self.l.compute())

    def __str__(self):
        return f'arcsin({self.l})'

    def str2(self):
        return "(" + "asin(" + self.l.str2() + ")" + ")"


class ArccosNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.acos(self.l.compute())

    def __str__(self):
        return f'arccos({self.l})'

    def str2(self):
        return "(" + "acos(" + self.l.str2() + "))"


class ArctgNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.atan(self.l.compute())

    def __str__(self):
        return f'arctg({self.l})'
    
    def str2(self):
        return "(atan(" + self.l.str2() + "))"


class ArcctgNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.pi / 2 - math.atan(self.l.compute())

    def __str__(self):
        return f'arcctg({self.l})'

    def str2(self):
        return "(acot(" + self.l.str2() + "))"


class ShNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.sinh(self.l.compute())

    def __str__(self):
        return f'sh({self.l})'

    def str2(self):
        return "(sh(" + self.l.str2() + "))"


class ChNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.cosh(self.l.compute())

    def __str__(self):
        return f'ch({self.l})'    

    def str2(self):
        return "(ch(" + self.l.str2() + "))"



class LogNode(ASTNode):
    def __init__(self, l):
        self.l = l

    def compute(self):
        return math.log(self.l.compute())

    def __str__(self):
        return f'log({self.l})'

    def str2(self):
        return "(log(" + self.l.str2() + "))"


class Log2Node(ASTNode):
    def __init__(self, l, r):
            self.l = l
            self.r = r

    def compute(self):
        return math.log(self.l.compute(), self.r.compute())

    def __str__(self):
        return f'(log({self.l}, {self.r}))'

    def str2(self):
        return "(log(" + self.l.str2() + "," + self.r.str2() + "))"


class VisualMathParser(sly.Parser):
    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        ('right', 'SIN', 'COS', 'TG', 'TAN', 'CTG', 'CTAN', 'COT',
               'ARCSIN', 'ASIN', 'ARCCOS', 'ACOS', 'ARCTG', 'ARCTAN', 'ATG', 'ATAN', 'ARCCTG', 'ACTG', 'ACTAN',
               'ARCCOT', 'LOG', 'LG', 'LN', 'SH', 'CH', 'SQRT'),
        ('left', '^'),
    )
    tokens = VisualMathLexer.tokens

    @_('NUMBER')
    def expr(self, p):
        return NumNode(p.NUMBER)

    @_('NAME')
    def expr(self, n):
        return VarNode(n.NAME);

    @_('E')
    def expr(self, n):
        return ENode()

    @_('PI')
    def expr(self, n):
        return PiNode()

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('"{" expr "}"')
    def expr(self, p):
        return p.expr

    @_('"[" expr "]"')
    def expr(self, p):
        return p.expr

    @_('expr "+" expr')
    def expr(self, p):
        return AddNode(p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return SubNode(p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return MinusNode(p.expr)

    @_('expr "*" expr')
    def expr(self, p):
        return MultNode(p.expr0, p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        return DivNode(p.expr0, p.expr1)

    @_('expr "^" expr')
    def expr(self, p):
        return PowNode(p.expr0, p.expr1)

    @_('SQRT expr')
    def expr(self, p):
        return SqrtNode(p.expr)

    @_('SIN expr')
    def expr(self, p):
        return SinNode(p.expr)

    @_('COS expr')
    def expr(self, p):
        return CosNode(p.expr)

    @_('TG expr', 'TAN expr')
    def expr(self, p):
        return TgNode(p.expr)

    @_('CTG expr', 'CTAN expr', 'COT expr')
    def expr(self, p):
        return CtgNode(p.expr)

    @_('ARCSIN expr', 'ASIN expr')
    def expr(self, p):
        return ArcsinNode(p.expr)

    @_('ARCCOS expr', 'ACOS expr')
    def expr(self, p):
        return ArccosNode(p.expr)

    @_('ARCTG expr', 'ARCTAN expr', 'ATG expr', 'ATAN expr')
    def expr(self, p):
        return ArctgNode(p.expr)
   
    @_('ARCCTG expr', 'ACTG expr', 'ACTAN expr', 'ARCCOT expr')
    def expr(self, p):
        return ArcctgNode(p.expr)

    @_('SH expr')
    def expr(self, p):
        return ShNode(p.expr)

    @_('CH expr')
    def expr(self, p):
        return ChNode(p.expr)

    @_('LOG expr', 'LN expr')
    def expr(self, p):
        return LogNode(p.expr)
    
    @_('LG expr')
    def expr(self, p):
        return Log2Node(p.expr, NumNode(10.0))
    
    @_('LOG "(" expr "," expr ")" ')
    def expr(self, p):
        return Log2Node(p.expr0, p.expr1)


def parse(s):
    lexer = VisualMathLexer()
    parser = VisualMathParser()
    s = s.lower()
    return parser.parse(lexer.tokenize(s))

def answer(s):
    result = parse(s)
    return result.str2()


allVariables = "a b c d"
for i in range(1, 22):
    allVariables += " " + chr(i + ord('e'))
a,b,c,d,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols(allVariables)


def check(studentStr, teachStr):
    setOfVar = set()
    for i in range(97, 123):
        setOfVar.add(i)
    a = sympify(answer(studentStr))
    b = sympify(answer(teachStr))
    if ((b - a) == 0):
        return 1
    listVarib = list(setOfVar)
    for i in range(0, len(listVarib)):
        listVarib[i] = (chr(listVarib[i]), 0.0)
    for step in range(0, 30):
        aComplete = False
        bComplete = False
        value = random.rand(1, len(listVarib))
        for i in range(0, len(listVarib)):
            listVarib[i] = (chr(97 + i), value[0][i])
        try:
            aVal = float(a.subs(listVarib))
            aComplete = True
        except Exception:
            aVal = 0
            aComplete = False
        try:
            bVal = float(b.subs(listVarib))
            bComplete = True
        except Exception:
            bVal = 0
            bComplete = False
        if ((not aComplete and bComplete) or (aComplete and not bComplete)):
            return 0
        if (abs(aVal - bVal) > 0.00001):
            return 0
    return 1
