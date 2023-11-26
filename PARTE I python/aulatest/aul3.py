perguntas ={
    'pergunta1':{'pergunta': 'quanto é 2+2?',
                'respostas':{'a':'1','b':'4','c': '5',},
                'resposta_certa':'b',
    },

    'pergunta2':{'pergunta': 'quanto é 3+2?',
                'respostas':{'a':'1','b':'4','c': '5',},
                'resposta_certa':'c',
    },
}

print()
resposta_certas=0
for pk,pv in perguntas.items():
    print(f"{pk}: {pv["pergunta"]}")

    for  rk,rv in  pv['respostas'].items():
        print(f"[{rk}] : {rv}")



    resposta_usuario=input("digite sua resposta")

    if resposta_usuario == pv['resposta_certa']:
       print('sua resposta esta correta ')
       resposta_certas +=1

    else:
        print("vish,vc errou")
print()

quantidade=len(perguntas)
porcetagensdeacerto=resposta_certas / quantidade * 100
print(f" vc acertou {resposta_certas} ")
print(f"sua porcentagem de acerto : foi {porcetagensdeacerto} %")      

































# LISTA = [[16, 25, 42, 7, 53, 16, 96, 33, 21, 5], 
#          [16, 16, 42, 42, 7, 8, 17, 3, 3, 5], 
#          [11, 225, 420, 7, 53, 16, 33, 22, 5], 
#          [16, 25, 42, 7, 53, 98, 16, 33, 16, 17]]

# def contador(lista_inteiro):
#     checknum = set()
#     primeiro_num = -1
    
#     for numero in lista_inteiro:
#         if numero in checknum:
#             primeiro_num = numero
#             break
#         checknum.add(numero)
        
#     return primeiro_num

# for lista in LISTA:
#     print(LISTA,contador(lista))


