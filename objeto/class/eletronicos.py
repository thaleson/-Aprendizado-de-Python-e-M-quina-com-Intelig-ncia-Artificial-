

class Eletronicos:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print("foi ligado ")
            return

        self._ligado = True

    def desligar(self):
        if  self._ligado:
            print('desligou')
            return
        self._ligado = False
