# n=int(input('digite seu numero'))

# numerosucesso=n+1
# numeroantecesso=n-1

# print(f"seu sucesso{numerosucesso},seu antecesso{numeroantecesso} ")



# usario=input('digite seu nome')
# idade=int(input('digite sua idade'))

# idade_maior=18
# idade_menor=30

# if idade >=idade_maior and idade<=idade_menor:
#     print(f"pode pegar emprestimo,{usario}")
# else :
#     print(f"nao pode pegar emprestimo")


n=input('digete aqui')
n2=input('digite aqui')
n.__len__()
print(len(n+n2))



# nome=input('digite seu nome')
# tamannho=len(nome)

# if tamannho <= 4:
#     print('seu nome é curto')

# elif tamannho <=6:
#      print('seu nome é normal')


# else:
#      print("seu nome é muito grande")





















week = input("digite um numero de 1-7,para eu informa o dia da semana , exe:1=domingo....")

if week.isdigit():
    week = int(week)

    if week  < 1 or week > 7:
        print("digite numero correto")
    else:
    
        if week == 1:
            print(" voce digitou 1 = domingo")

        elif week == 2:
            print(" voce digitou 2 = segunda-feira")

        elif week == 3:
            print(" voce digitou 3 = terça-feira")

        elif week == 4:
            print(" voce digitou 4 = quarta-feira")

        elif week == 5:
            print(" voce digitou 5 = quinta-fera")

        elif week == 6:
            print(" voce digitou 6 = sexta-feira")
        elif week == 7:
            print("voce digitou 7 = sabado")

else:
    print("isso não é um numero de uma semana")









