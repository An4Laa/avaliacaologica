senha = 1 # senha do usuário
print("\n" * 130) # simula uma pausa de tempo, como se o usuário tivesse esquecido de seu acesso e, consequentemente, sua senha


while senha != 2002: # este bloco compara a senha fixa com a tentativa de senha
    senha_tentativa = int(input("Digite sua senha: ")) # pede que o usuário insira sua senha
    if senha_tentativa != 2002: # se for diferente, mostra "senha invalida"
        print("Senha inválida.")
    else: # se for igual, mostra "acesso permitido"
        print("Acesso permitido.")
        break
