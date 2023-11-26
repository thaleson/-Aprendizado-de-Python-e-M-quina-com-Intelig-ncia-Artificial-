




lista=[
    {"nome":"luiz","idade":25},
    {"nome":"Moura","idade":35},
    {"nome":"joao","idade":55},
    {"nome":"felipe","idade":15},
    {"nome":"rose","idade":12},
    {"nome":"daniel","idade":75},

]

def lista2(nome):
   if nome["idade"] >=18:
    return (f"idade de maior{nome} ")
   else:
    return (f"idade menor{nome}")



novalista = map(lista2,lista)

for novalista2 in novalista:
 print(novalista2)

