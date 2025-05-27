"""L=[8,9,15]
for e in L:
    print(e)"""

def lista_defrutas():

    L=["maças", " peras", "kiwis"]
    for s in L:
        for letra in s:
            print(letra)
#lista_defrutas()

def numero_maior():
    L=[1,7,2,4,5,9,10,37,2,56,76,83,28,56,81]
    menor=L[11] 
    for e in L: 
        if e < menor:
            menor = e
    print(menor)
#numero_maior()

def pulando_numeros():
    for t in range(3,33,3):
     print(t, end=" ")
#pulando_numeros()

def composiçao():
    nome = "geovanna"
    idade = 17
    grana =15.00
    print("%s tem %d anos e R$%f no bolso." %(nome, idade, grana))
#composiçao()