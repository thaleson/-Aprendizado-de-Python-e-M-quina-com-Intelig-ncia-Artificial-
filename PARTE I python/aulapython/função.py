from aula8 import produtos,pessoas,lista 

novalista=map(lambda x : x  *   2,lista)
novalista=[x*2 for x in lista]

print(list(novalista))


for produtos in produtos:
    print(produtos)

    def aumeta_preco(p):
        p['preco'] = round(p['preco']*1.05)
        return p 

    produtos_novos=list(map(aumeta_preco,produtos))

    for produtos in produtos_novos:
        print(produtos) 



def filte_preco(pessoas):
     pessoas["idade"]=round(pessoas["idade"]*2)
     print  (f"nova idade {pessoas}") 
    
    
for pessoa in pessoas:
   

 nova_lista=filter(filte_preco,pessoas)

for listanova in nova_lista:
    print(listanova)


