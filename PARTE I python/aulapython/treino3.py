#############################################################
# PROGRAMA QLER EMPRESTIMO
from datetime import date
import time
casa = float(input("quanto é o valor da casa R$?"))
print("____" * 20)
salario = float(input("qaul salario do  comprador R$?"))
print("____" * 20)
anos = int(input("quanto tempo voce pretender finaciar?"))
print("____" * 20)
prestação = int(casa/(anos*12))
print("____" * 20)
minimo = salario*30/100

print(f"para pagar uma casa de {casa} em {anos} anos")
print(f"a prestação sera :{prestação}R$ reais  ")

time.sleep(2)
print("Processando....")
if prestação <= minimo:
    print("emprestimo aprovado")
else:
    print("emprestimo negado")
#############################################################

# PROGRAMA QUE LER NUMERO INTEIRO QUALQUER,E CONVERTE PARA BINARIO,OCTAL, HEXADECIMAL

import time


usario = int(input("digite um numero:"))

print("__" * 20)
print(f'''escolha uma das bases para conversão
          [1] converter para binario
          [2] converter para octal
          [3] converte para  hexadecimal''')
print("__" * 20)
opçaõ = int(input("SUA OPÇAO:"))

print("Processando...")
time.sleep(2)

if opçaõ == 1:
    print(f"seu {usario} convertido em binario: {bin(usario)}")
elif opçaõ == 2:
    print(f"seu {usario} convertido em octanario: {oct(usario)}")
elif opçaõ == 3:
    print(f"seu {usario} convertido em binario: {hex(usario)}")
##############################################################


##############################################################
#PROGRAMA DE NUMERO MAIOR
valor = int(input("digite um numero:"))
outro = int(input("digite outro numero: "))

if  valor > outro :
    print(f"o primeiro valor é maior")
elif outro > valor:
    print(f"o  segundo  valor e maior ")
elif  valor == outro:
   print("não existe valor maior , os dois são iguais ")

##############################################################


soldado = input("digite seu nome:")
nascimento = int(input("digite seu ano de nascimento:"))
ano = date.today().year
alistamento = ano-nascimento

if alistamento == 18:

    print(f"voce tem {alistamento},tem que se alistar no exercito")
elif alistamento < 18:
    saldo = 18 - alistamento
    print(f"voce tem {alistamento} anos , ainda n tem 18 anos para se alistar, falta {saldo} anos ")
elif alistamento > 18:
    saldo = alistamento-18
    print(f"voce tem { alistamento} anos , ja deveria te sido alistado a muito tempo, ah {saldo} anos ")
