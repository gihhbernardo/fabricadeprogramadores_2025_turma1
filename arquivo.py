try:    
    arquivo= open("arquivo.txt", "w")
    for linha in range(1,101):
        arquivo.write("%d\n"% linha)
    arquivo.close()
except:
    print("este arquivo infelizmente nao foi encotrado, tente mais tarde")








try:    
    arquivo=open("arquivo.txt","r") 
    for linha in arquivo.readlines():   
        print(linha)
    arquivo.close()
except:
    print("nao encontramos o arquivo")