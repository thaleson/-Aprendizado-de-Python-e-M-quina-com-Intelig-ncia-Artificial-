from dataclasses import dataclass


@dataclass

class Pessoa:
    nome:str
    sobrenome:str
    idade:int


p1=Pessoa('Paulo','Sérgio',36)

print(p1.nome)
print(p1.sobrenome)
print(p1.idade)