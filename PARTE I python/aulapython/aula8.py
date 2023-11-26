produtos = [
    {"nome": "Camiseta","preco": 50.9},
    {"nome": "short","preco": 500.9},
    {"nome": "regata","preco": 43.9},
    {"nome": "calça","preco": 30.9},
    {"nome": "calção","preco": 20.9},
    {"nome": "Tenis","preco": 550.9},
    {"nome": "Camisa","preco": 52.9},
]


pessoas =[
    {"nome":"luiz","idade":32},
    {"nome":"otavio","idade":22},
    {"nome":"jose","idade":12},
    {"nome":"joão","idade":42},
    {"nome":"Maria eduarda","idade":20},
    {"nome":"eduarda joana","idade":27},
    {"nome":"maria joaquina","idade":24},
]

lista=[1,2,3,4,5,6,7]


preco=1070.41

def aumenta_preco(valor,porcetagem):

  r = valor + round((valor*(porcetagem / 100)))
  return r
   
novopreco=aumenta_preco(valor=preco, porcetagem=40)   
print(novopreco)

