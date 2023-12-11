numeros = [] # lista de números inicialmente vazia, quando adicionados números positivos, acrescentaremos eles nesta lista
positivos = 0 # quantidade inicial de números positivos

for i in range(6):
    numero_teste = float(input(f"Digite o {i + 1}° número de sua lista: "))
    if numero_teste > 0:
        positivos += 1
        numeros.append(numero_teste)

soma = sum(numeros)
media = soma / positivos

print(f"{positivos} valores positivos")
print(f"{media}")
