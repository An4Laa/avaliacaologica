
def contar():
    contador = 0 # variável inicial, cujo valor equivale a "vazio"
    for i in range (1,6): # estrutura de repetição que repe
        n = int(input("Digite um valor inteiro: "))
    if n%2==0:
        contador+=1

    print(f"{contador} valores pares")

contar()