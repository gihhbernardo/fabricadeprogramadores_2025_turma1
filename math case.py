valor_parte= float(input("insira o valor a parte:"))
porcentagem= float(input("insira o valor da porcentagem"))
valor_total= valor_parte * (porcentagem/100)
print(valor_total)

valor_parte= float(input("insira o valor a parte:"))
porcentagem= float(input("insira o valor da porcentagem"))

match valor_parte:
    case 0:
        print("valor a parte nao pode ser zero")    
    case 1:
        print("valor a parte nao pode ser um")
    case 2:
        print("valor a parte nao pode ser dois")
