
      
'''valor_total=int(input())
porcentagem=15
valor_parte=valor_total* porcentagem/100
print("resultado da operaçao"+str(valor_parte))'''

'''valor_total=float(input("valor"))
porcentagem=float(input("valor"))
valor_parte=valor_total*porcentagem/100
print("resultado da operaçao:"+str(valor_parte)')'''


def triangulo():
 base =int(input("digite o valor ao lado:"))
 altura=int(input("digite o valor ao lado:"))
 area= (base * altura) /2
 print(area)
 return area
#triangulo()

def temperatura():
 c=int(input("digite o valor ao lado"))
 fahrenheit= (9*c+160)/ 5
 print(fahrenheit)
 return fahrenheit
#temperatura()

def valores():
    x=int(input("digite o valor ao lado"))
    y=int(input("digite o valor ao lado"))
    z=x
    x=y
    y=z
    print(x)
    print(y)
#valores()

def receba():
    comprimento=int(input("digite o valor ao lado"))
    altura=int(input("digite o valor ao lado "))
    largura=int(input("digte o valor ao lado"))
    volume=(comprimento *altura * largura)
    print(volume)
#receba()
    
def quadrado(lado):
   area=lado * lado 
   print(area)
   return area
def somadosquadrados():
    numero1=int(input())
    numero2=int(input())
    quadrado1=int(quadrado(numero1))
    quadrado2=int(quadrado(numero2))
    print(quadrado1+quadrado2)
somadosquadrados()