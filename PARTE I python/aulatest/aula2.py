for p,r in enumerate(range(10,0,-1)):
  print(p,r)

def mestre(func ,args,**kwargs):
     return func (args,**kwargs)

def fala_oi(nome , saudação):
   return f'oi {nome} {saudação}'

def saudação(nome,saudação):
 
    return f'{saudação} {nome}'

var=mestre(fala_oi,  "Alice",saudação="boa tarde")
var2=mestre(saudação,"thaleson" , saudação="boa noite")
print(var)
print(var2)

nome = "alice thaleson"  # Substitua "SeuNome" pelo seu nome.

for alice in range(10):
    print(nome)

   




