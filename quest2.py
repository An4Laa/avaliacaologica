salario = float(input("Digite seu salário atual: R$")) # recebe o valor do salário do funcionário

def aumento(): # função que vai calcular o valor do aumento de salário
    if salario <= 400:
        aumento_1 = (salario * 15) / 100 # calcula o novo salário do funcionário
        novo_salario_1 = salario + aumento_1
        print(f"Novo salário: {novo_salario_1:.2f}") # retorna o valor do novo salário
        print(f"Reajuste ganho: {aumento_1:.2f}") # retorna o valor do aumento
        print("Em percentual: 15%") # retorna o valor do percentual

    elif salario > 400 and salario <= 800:
        aumento_2 = (salario * 12) / 100
        novo_salario_2 = salario + aumento_2
        print(f"Novo salário: {novo_salario_2:.2f}")
        print(f"Reajuste ganho: {aumento_2:.2f}")
        print("Em percentual: 12%")
    
    elif salario > 800 and salario <= 1200:
        aumento_3 = (salario * 10) / 100
        novo_salario_3 = salario + aumento_3
        print(f"Novo salário: {novo_salario_3:.2f}")
        print(f"Reajuste ganho: {aumento_3:.2f}")
        print("Em percentual: 10%")

    elif salario > 1200 and salario <= 2000:
        aumento_4 = (salario * 7) / 100
        novo_salario_4 = salario + aumento_4
        print(f"Novo salário: {novo_salario_4:.2f}")
        print(f"Reajuste ganho: {aumento_4:.2f}")
        print("Em percentual: 7%")

    else:
        aumento_5 = (salario * 4) / 100
        novo_salario_5 = salario + aumento_5
        print(f"Novo salário: {novo_salario_5:.2f}")
        print(f"Reajuste ganho: {aumento_5:.2f}")
        print("Em percentual: 4%")
        
aumento() # retorna a função