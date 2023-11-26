# #LEITOR DE STRING EXERCICIO
# ########################################################################################
# import time
# from random import randint
# print('___' * 20)
# nome = input("digite seu nome: ")

# print(f"isso é uma numero  : {nome.isdigit()}")
# print(f"esse nome em menuscula: {nome.lower()}")
# print(f"esse nome em maiscula  : {nome.upper()}")
# print(f"QUANTAS letras tem no nome  :  {len(nome.replace(" ", ""))}")

# ########################################################################################
# # numero pra ver centena dezena milha

# print('___' * 20)

# numero = float(input("digite um numero: "))

# unidade = numero % 10
# dezena = (numero // 10) % 10
# centena = (numero // 100) % 10
# milhar = (numero // 1000) % 10

# print(f"Unidade: {int(unidade)}")
# print(f"Dezena: {int(dezena)}")
# print(f"Centena: {int(centena)}")
# print(f"Milhar: {int(milhar)}")


# #######################################################################################


# print('___' * 20)
# # nOME DA CIDADE

# # Verifica se os primeiros cinco caracteres (convertidos para maiúsculas) são iguais a "SANTOS"
# cidade = str(input(
#     'Qual o nome da cidade em que você nasceu?,tem santos nessa cidade?\n')).title().split()
# print('Santo' in cidade[0])
# #######################################################################################

# # Joguinho de adivinhação

# computador = randint(0, 5)
# print("====" * 20)
# print("vou pensar em numero entre 0 e 5,tenter adivinhar...")
# print("====" * 20)

# numero = int(input("em qual numero eu pensei ?"))
# print("Processando...")
# time.sleep(1)

# if numero == computador:
#     print("parabens vc consegiu me vencer")

# else:
#     print(f"ganhei eu pensei no {computador} e não no {numero} ")

# ########################################################################################


# ano = int(input("q ano é bissexto ?"))
# if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
#     print("é um ano bissexto")

# else:
#     print("não é bissexto")
# ########################################################################################


# funcionario = float(input("digite seu salario"))

# if funcionario <= 1250:
#     novo = funcionario+(funcionario*15/100)

# else:
#     novo = funcionario+(funcionario*10/100)
# print(f"quem gannhava {funcionario} passa a ganhar  agora : {novo}")


#######################################################################################

# sexo=input("digite seu nome")


from random import randint
import time


print('''
       opão : [M] Masculino
              [F] Feminino''')

sair=1
while sair != 0:
 sexo = input("digite o genero do usuario:").strip().capitalize().upper()        
 if sexo == "M":
   print("usario masculino")
 elif sexo == "F":
  print("usuario feminino")
 else:
  print("resposta invalida")
  sair = int(input("deseja continuar?[1-sim][0-nao]:"))
#######################################################################################


# Joguinho de adivinhação

from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. ')
        else:
            print('Menos... Tente mais uma vez. ')

print(f'Acertou com {palpites} tentativas. Parabéns!')

