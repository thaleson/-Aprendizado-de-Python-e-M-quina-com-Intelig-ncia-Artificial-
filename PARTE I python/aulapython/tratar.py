def converte_numero(valor):

    try:
        valor=int(valor)
        return valor
    except ValueError:
        try:
            valor=float(valor)
            return valor

        except ValueError:
            pass


while True :


            nummero=converte_numero(input('digite um numero'))

            if nummero is None:
                print('Erro:isso não é um numero')

            else:
                print(nummero * 10)


    print(a)
except MemoryError as erro:
    print('Erro de memória')
except NameError as erro:
    print('Variável não definida')


def divide(n1,n2):
  if n2 == 0:
    raise ValueError("erro nao pode ser 0")
  return n1/n2

try:
  print(divide(n1=2,n2=0))

except ValueError as  error:
print(divide(2,0))

class Tv:
    def __init__(self):
        self.ligada = False

    def ligar(self):
        if not self.ligada:
            print("tv esta ligada")
            self.ligada = True

    def desligar(self):
        if not self.ligada:
            print("tv desligada ")
            self.ligada = False
        else:
            print("a tv esta desligada")


minhatv = Tv()
# minhatv.ligar()
# minhatv.desligar()
# minhatv.desligar()
