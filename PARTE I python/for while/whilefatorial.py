n = int(input("Digite um número para ver o fatorial:"))

i = 2
resultado = 1

while i <= n:
    resultado *= i
    i += 1

print(f"O fatorial de {n} é {resultado}")
