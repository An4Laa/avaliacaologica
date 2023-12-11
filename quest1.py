renda = float(input("Digite sua renda atual: R$")) # recebe o valor

def imposto(): # função que vai calcular o valor do imposto de renda
    if renda <=2000.00: # verifica se valor do salário é menor ou igual a R$2000,00
        print("Você está ISENTO de taxa de imposto de renda") # retorna o valor isento
        
    elif renda > 2000.00 and renda <= 3000.00:
        imposto8 = (renda * 8) / 10 # calcula a porcentagem do salário do usuário
        print(f'Sua taxa do imposto de renda é de R${imposto8:.2f}') # ":.2f" delimita as casas decimais do resultado em duas
            
    elif renda > 3000.00 and renda <= 4500.00:
        imposto18 = (renda * 18) / 100
        print(f'Sua taxa do imposto de renda é de R${imposto18:.2f}')

    else:
        imposto28 = (renda * 28) / 100
        print(f'Sua taxa do imposto de renda é de R${imposto28:.2f}')

imposto() # retorna a função