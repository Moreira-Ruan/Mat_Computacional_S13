def calcular_salario(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos):
    # Calcula o salário inicial
    salario_final = salario_fixo

    if carros_vendidos > 0:
        # Adiciona a comissão por carro vendido
        salario_final += comissao_por_carro * carros_vendidos
        # Adiciona 5% sobre o total das vendas
        salario_final += 0.05 * total_vendas

        # Se o vendedor vender mais de 10 carros, adiciona o bônus de 10% sobre o total das vendas
        if carros_vendidos > 10:
            salario_final += 0.10 * total_vendas

    return salario_final

# Entrada de dados pelo usuário
salario_fixo = float(input("Digite o salário fixo mensal: "))
comissao_por_carro = float(input("Digite a comissão por carro vendido: "))
total_vendas = float(input("Digite o total das vendas realizadas: "))
carros_vendidos = int(input("Digite o número de carros vendidos: "))

# Calcula o salário final
salario_final = calcular_salario(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos)
print(f"Salário final: R$ {salario_final:.2f}")
