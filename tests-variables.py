from 
print(check("pi/4", "atg(1)"), "must be 1")
print(check("sin(pi/2)", "1"), "must be 1")
print(check("cos{pi/2}", "0"), "must be 1")
print(check("tg(-pi/4)", "4-5"), "must be 1")
print(check("ctg(-pi/5)", "tan(pi/2+pi/5)", ), "must be 1")
print(check("ctan(pi*98-2)", "cot(2-pi*2+100*\pi-4)"), "must be 1")
print(check("arcsin(0.7)", "asin(2-1.3)"), "must be 1")
print(check("9*arccos(-89+89.2)", "[10-1]*acos(0.2)"), "must be 1")
print(check("arctg(31)", "cos{0}*arctan(32-1)"), "must be 1")
print(check("atg(-21)-21", "-21 + atan(-321+300)"), "must be 1")
print(check("arcctg9-12", "23+actg(8+21-4*5)-35"), "must be 1")
print(check("actan(-900)*90", "90.0*arccot(-8*9000/80)"), "must be 1")
print(check("log(7, 10)", "lg(9-2.0)"), "must be 1")
print(check("ln(e)", "log(\e*pi/\pi)"), "must be 1")
print(check("arccos(sqrt[3]/2)", "pi/6"), "must be 1")
print(check("3", "2 + 1"))
wrong = 0
if (check("sin(a)+cos(2.1)*e^2", "cos(\pi/2.0-a)*cos(0)+cos(-21*0.1)/e^{-2}") != 1):
    wrong += 1
if (check("arcsin(20*s-10^b)+12*pi/ln(b)", "-asin(e^(ln10*b)-s*40/2)+pi/log(b)*12") != 1):
    wrong += 1
if (check("arccos(b-lg(a))", "acos(b-[ln(a)/log(10)])") != 1):
    wrong += 1
if (check("tg(d+10*pi)", "tan({0.1*1/\pi}^cos(pi)+ d)") != 1):
    wrong += 1
if (check("ctg(f-cos(g))", "ctan[-cos(g)+f]") != 1):
    wrong += 1
if (check("(i+j)^2-2*j*i", "i^ln(\e^2)+sqrt(j^4)") != 1):
    wrong +=1
if (check("arctan[70-k*sqrt(l+n)]-arccot(n*0.02)","atan{70-k*(n+l)^0.5}-arccot(n/5/10)") != 1):
    wrong += 1
if (check("arccot(o)-log(sqrt(p*\pi-e))", "-lg{p*pi-\e}^0.5*ln(10)+actan(1*o)") != 1):
    wrong += 1
if (check("ctan(z-h)+e^sqrt(f)+790*tg(1)", "cot(h-z)+e^{f^0.5}+790/4*pi") != 0):
    wrong += 1
if (wrong > 0):
    print("bad result")
else:
    print("all tests passed")
