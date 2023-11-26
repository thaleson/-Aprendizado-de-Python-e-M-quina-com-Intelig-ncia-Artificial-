
# #SEGMENTOS DE TRIANGULOS
# ############################################################################################
# from datetime import date
# import time

# print('-=' *20 )
# r1=int(input("digite comprimento da reta:"))
# r2=int(input("digite comprimento da reta2:"))
# r3=int(input("digite comprimento da reta3:"))

# print("Processando.....")
# time.sleep(2)

# if r1 < r2+r3 and  r2 < r3+r2  and  r3 < r2+r1:
#     print ("os segmentos acima podem formar um triangulo")
# else:
#     print("os segmentos acima , não formam um triangulo")
# ############################################################################################

# #PROGRAMA DE NOTAS

# aluno=input("digite seu nome:")
# nota1=float(input("digite sua primeira nota:"))
# nota2=float(input("digite sua segunda nota:"))
# resultado=nota1+nota2/2

# if resultado <= 5.0:
#     print(f"voce {aluno} foi reprovado com media: {resultado}")
# elif resultado  <= 6.9:
#     print(f"voce aluno(a) {aluno} com media {resultado}, esta em recuperação ")
# elif  resultado >= 7.0:
#     print(f"parabens aluno(a) {aluno}, voce foi aprovado com media :{resultado}")

# ############################################################################################

# #programa de confederação de natação

# atleta=input("digite seu nome:")
# print("===" *20 )
# nascimento=int(input("digite ano do seu nascimento:"))
# data=date.today().year
# idade=data-nascimento


# print("Processando....")
# time.sleep(2)

# if idade <= 9:
#     print (f"o atleta {atleta} tem {idade} anos é da categoria :MIRIM")
# elif idade <=14:
#     print(f"o atleta {atleta} tem {idade} anos, é da categoria :Infatil")
# elif idade <=19:
#     print(f"o atleta {atleta} tem {idade}anos, é da categoria : Senior")
# elif idade >=20:
#     print(f"o atleta {atleta} tem {idade}anos, é da categoria :Master")
###########################################################################################
#Imc

nome=input("digite seu nome:")
altura=float(input("digite sua altura:"))
peso=float(input("digite seu peso:"))
imc=(peso/(altura*altura))
     
if imc <=18.5:
    print(f"voce {nome}, tem imc :{imc} e  esta abaixo do peso")
elif 18.5 <= imc < 25:
    print(f"voce {nome} , tem imc :{imc},esta no peso ideal")
elif 25<= imc  <30:
    print(f"voce {nome}, tem imc :{imc}, Sobrepeso")
elif  30 <=  imc < 40:
    print(f"voce {nome},tem imc:{imc}, obesidade")
elif imc >= 40 :
    print(f"voce {nome} , tem imc {imc:}, morbida")
###########################################################################################


# import random
# import time


# print('==='*5, "Lojas americanas ", '==='*5)


# usuario = input("Ola,digite seu nome:")


# print("_________" * 10)


# produto = float(input("digite preço do produto:"))

# print('''' opçoes :
#       [1] a vista/pix
#       [2] cartao avistar
#       [3] 2vezes no cartao
#       [4] 3 vezes no cartão ou mais 
#        ''')
# opção = int(input("digite sua opção:"))

# if opção == 1:
#     a_vista = produto - (produto*10/100)
#     print(f"{usuario}, o valor do produto com desconto a vista é:{a_vista}Reais")
# elif opção == 2:
#     cartão_avista = produto - (produto * 5/100)
#     print(f"{usuario}, o valor do produto a vista com desconto  é:{cartão_avista}")
# elif opção == 3:
#     normal_preco = produto/2
#     print(f"{usuario}, o valor do produto sem nenhum desconto 2x no cartão fica:{ normal_preco}")
# elif opção == 4:
#     cartao_juros = produto + (produto * 20/100)
#     total = int(input("digite quantas parcelas ?"))
#     totalapagar = int(cartao_juros/total)
#     print(f"suas compras sera parcelado em {total}vezes de {totalapagar}R$ REAIS com juros  ")
#     print(f"{usuario},sua compra de :{produto}, vai ficar {cartao_juros} no final")
# else:
#     print("opcao invalida de pagamento, tente novamente ")
# ############################################################################################
# #joguinho do jock pow

# jogador = input("digite seu nome:")
# print('''jogo pedra papel e tesoura
#       [1]Tesoura
#       [2]Papel
#       [3]Pedra''')
# opção = int(input("digite sua opção para joguinho começa:"))

# computador = random.randint(1, 3)
# itens = {1: 'Tesoura', 2: 'Papel', 3: 'Pedra'}
# print(f"O computador jogou {itens[computador]}")
# print(f"O jogador jogou {itens[opção]}")
# print("Processando")
# time.sleep(1)

# if computador == 3:  # PC jogou pedra

#     if opção == 3:
#         print("empate")
#     elif opção == 2:
#         print(f"{jogador},venceu")
#     elif opção == 1:
#         print("vc perdeu, o computador escolheu pedra")

# elif computador == 2:  # pc jogou pedra
#     if opção == 3:
#         print(f"pc venceu,ele escolheu papel")
#     elif opção == 2:
#         print("empate")
#     elif opção == 1:
#         print(f"vc {jogador} ,venceu")
# elif computador == 1:  # pc jogou tesoura
#     if opção == 3:
#         print(f"voce {jogador} venceu ")
#     elif opção == 2:
#         print(f"o computador escolhe:tesoura, ele venceu")
#     elif opção == 1:
#         print("empate")
