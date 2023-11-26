from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever
from classes import Cliente,Endereço

escritor=Escritor('antonio')
caneta=Caneta('bic')
maquinadeescrever=MaquinaDeEscrever()

escritor.ferramenta=caneta
escritor.ferramenta.escrever()
print('==' *20)
escritor.ferramenta=maquinadeescrever
escritor.ferramenta.escrever()
print('==' * 20)
escritor.ferramenta=escritor

escritor.ferramenta.escrever()
print('==' * 20)

cliente1=Cliente('Alice',26)
print(cliente1.nome)
cliente1.insira_endereço('Ceara mirim','RN')
cliente1.list_endereço()
print('====' *15)
cliente2=Cliente('Aracy',26)
print(cliente2.nome)
cliente2.insira_endereço('Natal', 'RN')
cliente2.list_endereço()
print('====' * 15)
cliente3=Cliente('thaleson',26)
print(cliente3.nome)
cliente3.insira_endereço('CALIFONIA','ESTADOS UNIDOS DA AMERICA')
cliente3.list_endereço()
print('====' * 15)
cliente1.list_endereço()
print('====' * 15)