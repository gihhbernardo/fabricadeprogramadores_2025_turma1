import math
def delta():
    a=float(input("insira um valor coeficinete:"))
    b=float(input("insira um valor coeficinete:"))
    c=float(input("insira um valor coeficinete:"))
    delta_resultado= b**2- 4*a*c
    if delta_resultado >=0.0:   
        raiz1=(-b + math.sqrt(delta_resultado))/(2*a)
        raiz2=(-b - math.sqrt(delta_resultado))/(2*a)  
        print("o resultado" , raiz1 , "e" , raiz2 )
    else:
        print("essa ecuaçao nao possui raizes reais")
delta()