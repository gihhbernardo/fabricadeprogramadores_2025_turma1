a=True
b=False
c=True
print(a and a)
print(b and b)
print(not c)
print(not a)
print(a and b)
print(b and c)
print(a or c)
print(not b)

valor_parte= float(input("insira o valor a parte:"))
porcentagem= float(input("insira o valor da porcentagem"))
valor_total= valor_parte * (porcentagem/100)
print(valor_total)

valor_parte= float(input("insira o valor a parte:"))
porcentagem= float(input("insira o valor da porcentagem"))
if  porcentagem <=0.0:
    print("insira um numero maior que 0")
else:
    valor_total= valor_parte * (porcentagem/100)
    print(valor_total)

nota1=int(input("digite a primeira nota"))
nota2=int(input("digite a segunda nota"))
nota3=int(input("digite a terceira nota"))
nota4=int(input("digite a quarta nota"))
media=(nota1+nota2+nota3+nota4)/4
presença=int(input("dias que ele veio"))
valor_total= presença * (75/365)
if (media >= 6) and (valor_total >=0.75) :
    print("aprovado")
else:
    print("reprovado")
