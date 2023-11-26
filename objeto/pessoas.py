from datetime import datetime
from random import randint

# Em Python, a palavra-chave "class" é usada para criar uma classe,
# que é uma estrutura que permite criar objetos. Uma classe é uma
# espécie de modelo para objetos, e os objetos são instâncias dessa classe.
#  As classes são uma parte fundamental da programação orientada a objetos (OOP) em Python.


class Pessoas:
    ano_atual = int((datetime.strftime(datetime.now(), '%Y')))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome}, ja esta comendo ")
            return
        print(f"{self.nome} esta comendo {alimento}")
        self.comendo = True

    def paradecomer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo ")
            return
        print(f"{self.nome} parou de comer ")
        self.comendo = False

    def voltaacomer(self):
        if self.comendo:
            print(f"{self.nome} voltou a comer")
            return
        print(f"{self.nome} voltou a comer")
        self.comendo = True

    def falando1(self, falando):
        print(f"{self.nome} esta falando {falando} ")
        self.falando = True

    def idadetrue(self, maior):
        print(f"A menina  {self.nome} ela é maior de idade ela tem : {
              self.idade}anos , ela é de {maior}")

    def idadeatual(self):
        return self.ano_atual - self.idade
 ##################################################################################
 # Em Python, o decorador @classmethod é usado para criar um método de classe.
 # Um método de classe é associado à classe em vez de uma instância específica dessa classe.
 # Ele é definido usando a palavra-chave classmethod antes da declaração do método.

    @classmethod
    def get_ano_de_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual-ano_nascimento
        return cls(nome, idade)

# Em Python, o decorador @staticmethod é usado para criar um método estático.
# Um método estático é um método associado à classe, mas que não tem acesso
# ao objeto ou à instância específica da classe. Isso significa que ele não
# recebe uma referência à instância (self) ou à classe (cls) como seu primeiro argumento.
    @staticmethod
    def gera_id():
        randi = randint(100000, 10000000)
        return randi
