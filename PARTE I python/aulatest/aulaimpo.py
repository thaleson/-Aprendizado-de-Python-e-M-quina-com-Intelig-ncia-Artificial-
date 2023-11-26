cliente1= {
    'cliente 1 ':{
        'nome':'joão',
        'sobrenome':'luiz'

    },
    'cliente 2 ':{
        'nome':'Alice',
        'sobrenome':'Maria'

    },
    'cliente 3 ':{
        'nome':'Aracy',
        'sobrenome':'silva'

    },
    'cliente 4 ':{
        'nome':'Deodoro',
        'sobrenome':'silva'

    },
    'cliente 5 ':{
        'nome':'Tiago',
        'sobrenome':'silva'

    },
    'cliente 6 ':{  
        'nome':'josi',
        'sobrenome':'Maria'

    },
}

for cliente_k,cliente_v in cliente1.items():
  

  print()
  
  print(f"exibindo {cliente_k}")

  for dados_k,dados_v in cliente_v.items():

    print(f"{dados_k}={dados_v}")



