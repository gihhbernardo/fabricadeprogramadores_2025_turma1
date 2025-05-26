L=[]
soma= 0
while True:
   v=int(input("digite um numero ou 0 para sai:"))  
   if v == 0:
      break
   soma = soma + v
   L.append(v)
x = 0
while x < len(L):
   #print(L[x])
   x = x+1
print(L)
print("a soma é:",soma," e a media é ", soma/len(L))
