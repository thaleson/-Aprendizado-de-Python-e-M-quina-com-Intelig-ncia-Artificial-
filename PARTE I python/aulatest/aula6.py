


from itertools import combinations,permutations,product,groupby 
alunos=[

  {'nome':'ALUNOA','nota': 'A'} ,
  {'nome':'ALUNOB','nota': 'D'} ,
  {'nome':'AlunoC','nota': 'B'} ,
  {'nome':'AlunoD','nota': 'F'} ,
  {'nome':'AlunoE','nota': 'A'} ,
  {'nome':'AlunoF','nota': 'A+'} ,
  {'nome':'AlunoG','nota': 'F'} ,
  {'nome':'AlunoH','nota': 'C'} ,
  {'nome':'AlunoI','nota': 'D'} ,
 ]

ordena= lambda item:item['nota']
alunos.sort(key=ordena)
alunos_agrupados=groupby(alunos,ordena)

for agrupamentos ,valores_agrupados in alunos_agrupados:

 print(f'agrupamento{agrupamentos}')
 for aluno in valores_agrupados:
  print(aluno)

  print()