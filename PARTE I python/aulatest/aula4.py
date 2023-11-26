# nome= ['Alice','Aracy','Josi']

# ex=[v.replace('A','T') for v in nome]

# print(ex)





string='012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'


n=10
contadores= [i  for i in  range(0,len(string), n)]
tuplas=[(i,i + n) for i in range(0,len(string),n)]
lista=[string[i:i + n ] for i in range (0,len(string),n)]
raw=[f'string[{i}:{i+n}]' for  i in range(0,len(string),n)]
retorno='.'.join(lista)
# jorg=[v.replace("0","salve ") for v in string]
print(retorno)
print(lista)
print(raw)
