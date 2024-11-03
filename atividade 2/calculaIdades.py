def calcular_soma_produto(idade_homem1, idade_homem2, idade_mulher1, idade_mulher2):
    # Validando se as idades são números inteiros positivos
    if not all(isinstance(idade, int) and idade > 0 for idade in [idade_homem1, idade_homem2, idade_mulher1, idade_mulher2]):
        return "Erro: Todas as idades devem ser números inteiros positivos."

    # Identificando o homem mais velho e o homem mais novo
    homem_mais_velho = max(idade_homem1, idade_homem2)
    homem_mais_novo = min(idade_homem1, idade_homem2)

    # Identificando a mulher mais velha e a mulher mais nova
    mulher_mais_velha = max(idade_mulher1, idade_mulher2)
    mulher_mais_nova = min(idade_mulher1, idade_mulher2)

    # Calculando a soma e o produto conforme as regras
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha

    return soma, produto

# Entrada de dados pelo usuário
try:
    idade_homem1 = int(input("Digite a idade do primeiro homem: "))
    idade_homem2 = int(input("Digite a idade do segundo homem: "))
    idade_mulher1 = int(input("Digite a idade da primeira mulher: "))
    idade_mulher2 = int(input("Digite a idade da segunda mulher: "))

    resultado = calcular_soma_produto(idade_homem1, idade_homem2, idade_mulher1, idade_mulher2)

    if isinstance(resultado, str):
        print(resultado)
    else:
        soma, produto = resultado
        print(f"Soma da idade do homem mais velho com a mulher mais nova: {soma}")
        print(f"Produto da idade do homem mais novo com a mulher mais velha: {produto}")

except ValueError:
    print("Erro: Por favor, insira valores inteiros válidos para as idades.")
