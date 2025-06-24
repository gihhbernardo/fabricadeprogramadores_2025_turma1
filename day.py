import sys,os
print("numero de parametros:%d" % len(sys.argv))
for n,p in enumerate(sys.argv):
    print("parametro %d = %s"% (n,p))
    try:
        os.mkdir(p)
    except FileExistsError:
        print(f"""\033[0;32m pasta '{p}nao encontrada...""")
    except OSError:
        print(f"""\033[0;32m pasta '{p}é um arquivo, não uma pasta!!""")


