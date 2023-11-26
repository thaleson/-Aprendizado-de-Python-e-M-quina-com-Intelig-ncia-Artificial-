
class Banco:
    def __init__(self, nome, conta):
        self.nome = nome
        self.conta = conta
        self._depositarr = 0
    
    @property
    def depositar(self):
     self._depositarr=0
     return
     
    
    def depositar2(self, valor):

        self._depositarr += valor
        print(f"voce depositou :{valor} reais")

    def saque(self, valor):
        self._depositarr -= valor
        print(f"voce sacou :{valor} reais")

    def versaldo(self):
       
       print(f"seu saldo atual é :{self._depositarr}")
       return
    
    def detalhes(self):
       print(f"seu  nome é {self.nome}")
       print(f"sua conta é {self.conta}")
       print(f"e seu saldo é  {self._depositarr}")
       print(f"seu sexo é :{self.sexo}")
       return

              
