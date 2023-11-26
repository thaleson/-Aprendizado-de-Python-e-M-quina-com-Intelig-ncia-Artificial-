#TOTAL DE EXERCICIOS= 20 

##########################################################################################
#DIZ se string ou n varias formas
digitealgo=input("digite algo")

print(f"o tipo desse valor é : {type(digitealgo)}")

if digitealgo.isdigit():
   print("a string representa um numero")

else:
    print("a string não representa um numero ")

if ' ' in digitealgo:
    print("A string contém espaço.")
else:
    print("A string não contém espaço.")

if digitealgo.replace(".", "", 1).isdigit():
    try:
        numero = float(digitealgo)
        print(f"{numero} é um número.")
    except ValueError:
        print("A string não representa um número.")
else:
    print("A string não representa um número.")

##########################################################################################
#DOBRO triplo e raiz :
import math
numero=int(input("digite um numero"))


dobro= numero * 2
Triplo= numero * 3
raiz_quadrada=math.sqrt(numero)
print(f" o {numero} é")
print(f"seu dobro é {dobro}")
print(f"seu triplo é {Triplo}")
print(f"sua raiz quadrada é : {raiz_quadrada}")


aluno=input("Digite seu nome")
nota1=float(input("digite sua primeira nota"))
nota2= float(input("digite sua segunda nota"))

media=(nota1+nota2)/2


print(f"sua primeira nota foi :{nota1},sua segunda nota foi :{nota2}, e sua media foi: {media}")

###########################################################################################
#PROGRAMA tabuada:
tabuada = float(input("Digite um número para ver a tabuada: "))

print('___'*12)

print("tabuada ")

print(f"{int(tabuada)} x 1 = {int(tabuada * 1)}")
print(f"{int(tabuada)} x 2 = {int(tabuada * 2)}")
print(f"{int(tabuada)} x 3 = {int(tabuada * 3)}")
print(f"{int(tabuada)} x 4 = {int(tabuada * 4)}")
print(f"{int(tabuada)} x 5 = {int(tabuada * 5)}")
print(f"{int(tabuada)} x 6 = {int(tabuada * 6)}")
print(f"{int(tabuada)} x 7 = {int(tabuada * 7)}")
print(f"{int(tabuada)} x 8 = {int(tabuada * 8)}")
print(f"{int(tabuada)} x 9 = {int(tabuada * 9)}")
print(f"{int(tabuada)} x 10 = {int(tabuada * 10)}")


##########################################################################################

#CARTEIRA e conversor de moeda

carteira=float(input("quanto dinhero voce tem na sua carteira ?"))

coverto=(carteira/4.91)
convertoEuro = (carteira/5.26)
convertoIene = (carteira/1)

print(f"o dinheiro da sua carteira é {int(carteira)} reais, com esse dinherio vc compra {int(coverto)}US$ dolares")
print(f"o dinheiro da sua carteira é {int(carteira)} reais, com esse dinherio vc compra {int(convertoEuro)}€ Euros")
print(f"o dinheiro da sua carteira é {int(carteira)} reais, com esse dinherio vc compra {int(convertoIene)}¥ yen")

##########################################################################################
#EXERCICIO da altura e largura 

largura=float(input("digite a largura"))
altura=float(input("digite a altura"))

area= largura * altura
tinta=area/2
print(f"sua parede tem dimensão de {largura}x{altura} e sua area total é de {area}m²")
print(f"voce precisara de {tinta}L de tinta")


##########################################################################################

#SALARIO : aqui em baixo (porcentagem)


Produto=float(input("qual salario do funcionario ?"))


descontofinal=Produto + (Produto*15/100)

print(f"funcionario ganhava  {Produto}, com aumento de 15% ele fica {descontofinal:.2f}")
##########################################################################################

#exercicios dias:
dias=float(input("digite quantos dias "))
Km=int(input("quantos km rodado"))

pagar= (60 *dias)+ (Km*0.15 ) 

print(f"o total a pagar é de {pagar}R$")

##########################################################################################

#EXERCICIO DO NUMERO REAL PRO INTERIO 

import math
n=float(input("digite um numero "))

inteiro=int(n)

print(f" seu numero real {n} covertido para inteiro seria {inteiro}")


#Ângulo em radianos
angulo = math.radians(90)  # Substitua 45 pelo ângulo desejado em graus

# Seno
seno = math.sin(angulo)
print(f"Seno: {seno}")

# Cosseno
cosseno = math.cos(angulo)
print(f"Cosseno: {cosseno}")

# Tangente
tangente = math.tan(angulo)
print(f"Tangente: {tangente}")
#########################################################################################

#SORTEIA EXERCICIO

import random

#Solicitar a entrada do nome de cada aluno
aluno1 = input("Nome do aluno A: ")
aluno2 = input("Nome do aluno B: ")
aluno3 = input("Nome do aluno C: ")
aluno4 = input("Nome do aluno D: ")

# Criar uma lista com os nomes dos alunos
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

# Sortear um aluno aleatório da lista
# aluno_sorteado = random.choice(lista_alunos)
random.shuffle(lista_alunos)
print(f"a ordem foi :{lista_alunos} ")
# print(f"Aluno sorteado: {aluno_sorteado}")

