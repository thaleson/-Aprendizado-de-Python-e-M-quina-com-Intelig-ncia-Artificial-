from banco2 import Banco


class Pessoa(Banco):
    def __init__(self, nome, idade, sexo,conta):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.conta=conta
        super(). __init__(nome,conta)