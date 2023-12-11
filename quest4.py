import time # importa o tempo da biblioteca
print("Olá! Para qual ddd deseja discar?") # pergunta ao usuário qual o ddd desejado
time.sleep(1) # dá um espaço de um segundo até que a próxima interação seja solicitada
numero = int(input("Digite aqui: ")) # pede que o usuário informe o número do ddd

def ddd(): #
    if numero == 61:
        print("Brasília")

    elif numero == 71:
        print("Salvador")
    
    elif numero == 11:
        print("São Paulo")

    elif numero == 21:
        print("Rio de Janeiro")

    elif numero == 32:
        print("Juiz de Fora")

    elif numero == 19:
        print("Campinas")

    elif numero == 27:
        print("Vitória")

    elif numero == 31:
        print("Belo Horizonte")

    else:
        print("DDD não cadastrado")

ddd() # retorna a função