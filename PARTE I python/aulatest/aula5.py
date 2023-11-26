from itertools import count 
carrinho=[]


carrinho.append(('produto2',50))
carrinho.append(('produto3',100))
 
tolta=sum((float (y) for  x,y in carrinho))

print(tolta)




lista1 = [1, 2, 3,5,8,9]
lista2 = [4, 5, 6]
lista_somada = [x + y for x, y in zip(lista1, lista2)]
print(lista_somada)






contador=count(start=1000 , step=10  )

for valor  in contador:
    print(valor)

    if valor >= 10000 :
      break