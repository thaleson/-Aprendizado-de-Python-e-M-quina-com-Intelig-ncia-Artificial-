# Usuario=input("digite um nome de um pais:")

# lista = {'Portugal': 'Lisboa.', 'Argentina': 'Bueno Ares',
#          'Alemanha': 'Berlim', 'Japão': 'Tóquio'}


# if Usuario in lista:
#      print(f"a capital desse pais  {Usuario} é: {lista[Usuario]}")
# else:
#      print("não temos informação sobre esse pais ")  


# ##############################################################################

# # exerciicos random


# lista1 = ['luiza', 'pedro', 'joão', 'aracy']
# lista2 = ['luiza', 'zezo', 'diego', 'aracy']

# nomes_comuns = set(lista1).intersection(lista2)



# print("Nomes iguais nas duas listas:", list(nomes_comuns))

##############################################################################

u=lambda num: 'par'if num %2 ==0  else 'impar'

us=int(input("digite um numero:"))



print(f"é par ou impar:{u(us)}")