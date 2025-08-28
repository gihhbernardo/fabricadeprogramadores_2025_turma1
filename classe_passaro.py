class Passaro():
    
    def __init__(self,tamanho,cores,especie,sexo):
        self.tamanho = tamanho
        self.core = cores
        self.especie = especie
        self.sexo = sexo
    
    def cantar(self):
        return print(f'sou um{self.especie} cantando uma bela canção')
    
    def voar(self):
        return print('bater asas e: voando...')
    
passaro1 = Passaro(0.14,['marrom','branco','cinza'], 'pardal', "m")
Passaro.cantar(self)