
# Relações entre objetos (conversa uma classe com a outra)
# relação de ASSOCIAÇÃO
# UMA CLASSE Q ASSOCIA A OUTRA

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

    def escrever(self):
        print(f"o escritor estar escrevendo")


class Caneta:
    def __init__(self, marca):

        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print(f"a caneta escreve")


class MaquinaDeEscrever:
    def escrever(self):
        print(f"a maquina esta  escrevendo ")


#######################################################################

# Agregação orientação e objeto
class Carrinhodecompra:
    def __init__(self):
        self.produtos = []

    def inserir_product(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produtos in self.produtos:
            total += produtos.valor

        return total

    def deleteitem(self, nome, valor):
        del self.produtos[nome, valor]


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


################################
# composição de objeto

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insira_endereço(self, cidade, estado):
        self.enderecos.append(Endereço(cidade, estado))

    def list_endereço(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereço:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
#######################################################################
# HERANÇAS SIMPLES CLASSES


class Pessoa:
    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falaoi(self):
        print(f" {self.nomeclasse} falou oi")

    def falaidade(self):
        print(f"minha idade é {self.idade}")


class Cliente(Pessoa):
    def comprando(self):
        print(f" {self.nomeclasse}  comprando....")

    def ligandoocarro(sefl):
        print(f"{sefl.nome} esta ligando o carro")
class Aluno(Pessoa):
    def bebendo(self):
        print(f" {self.nome} esta bebendo...")


class ClienteVip(Cliente):

    pass
