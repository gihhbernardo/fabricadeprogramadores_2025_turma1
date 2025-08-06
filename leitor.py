import csv 
nome_do_arquivo= 'OCORRENCIAS_2024.csv'
Pistola=0
Garruchao = 0
Garrucha = 0
Fuzil = 0
Espingarda = 0
Pistolao = 0
Revolver = 0
Rifle = 0
Carabina = 0
try:
    exemplo_arquivo= open (nome_do_arquivo)
    exemplo_leitor= csv.reader(exemplo_arquivo,
                               delimiter=';',
                               dialect='excel')
    for linha in exemplo_leitor:
        '''print('linha #%/s <%s>'
        %(exemplo_leitor.liner_num, linha ))'''
        if linha[4].strip(" ")== "Pistola":
            Pistola += 1
        elif  linha[4].strip(" ")== "Garruchao":
            Garruchao += 1
        elif  linha[4].strip(" ")== "Garrucha":
            Garrucha += 1
        elif  linha[4].strip(" ")== "Fuzil":
            Fuzil += 1
        elif  linha[4].strip(" ")== "Espingarda":
            Espingarda += 1
        elif  linha[4].strip(" ")== "Pistolao":
            Pistolao += 1
        elif  linha[4].strip(" ")== "Revolver":
            Revolver += 1
        elif  linha[4].strip(" ")== "Rifle":
            Rifle += 1
        elif  linha[4].strip(" ")== "Carabina":
            Carabina += 1
    exemplo_arquivo.close()
except FileExistsError:
    print('arquivo nao encontrado')
    print(exemplo_arquivo)