import json 
dados_json= {"nome": "geovanna", "e-mail" :"geovanna@gmail "}

dados_jsona= json.dumps(dados_json)

with open("pessoa.json", "a") as arquivo:
    arquivo.write(dados_jsona)
