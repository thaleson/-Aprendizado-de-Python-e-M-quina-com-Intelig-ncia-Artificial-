n = int(input("Digite um numero: "))
d = int(input("Digite outro numero: "))
sair = 0

while sair != 5:
    print('''Opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números 
    [5] Sair do programa''')

    opcao = int(input("Escolha a opção desejada: "))
    if opcao == 1:
        print(f"O resultado da soma dos seus dois números é {
              n} + {d} = {n + d}")
        print("====="*10)

    elif opcao == 2:
        print(f"O resultado da multiplicação entre {n} x {d} = {n * d}")
        print("====="*10)

    elif opcao == 3:
        if n > d:
            print(f"{n} é maior que {d}")
        elif d > n:
            print(f"{d} é maior que {n}")
        else:
            print("Os números são iguais.")
    elif opcao == 4:
        print("Novos números:")
        n = int(input("Digite um novo número: "))
        d = int(input("Digite outro novo número: "))
        print("====="*10)

    elif opcao == 5:
        print("Saiu do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
