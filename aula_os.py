import os 

'''os.getcwd()
print(os.getcwd())

os.mkdir("d")
os.mkdir("e")
os.mkdir("f")'''

arquivo_="f"
try:
    os.rmdir(arquivo_)    
    print(f"""\033[0;32m pasta '{arquivo_}removida com sucesso!""")
except FileExistsError:
    print(f"""\033[0;32m pasta '{arquivo_}nao encontrada...""")
except OSError:
    print(f"""\033[0;32m pasta '{arquivo_}é um arquivo, não uma pasta!!""")
#arquvivo_



arquivo_path="texto1"
try:
    os.remove(arquivo_path)    
    print(f"""\033[0;32m pasta '{arquivo_path}removido com sucesso!""")
except FileExistsError:
    print(f"""\033[0;32m pasta '{arquivo_path}nao encontrado...""")
except OSError:
    print(f"""\033[0;32m pasta '{arquivo_path}é uma pasta , não um arquivo!!""")
    