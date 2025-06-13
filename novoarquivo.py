def lê_binário():
    try:
        with open("binary.jpg" ,"rb") as fs1:       
                    dados=fs1.read()
        for linha in range(0,50):
            with open(( "cópia %d.jpg" % linha),"wb") as fs2:
                 fs2.write(dados)
    except IOError :
        print('Deu algo errado @_@') 
    print("OK! ~_~")
lê_binário()
