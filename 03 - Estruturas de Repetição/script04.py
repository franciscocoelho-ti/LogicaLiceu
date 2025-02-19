# Escreva um algoritmo em Python que receba do usuário 8 números, e imprima a soma dos números impares que foram informados.

soma = 0

for num in range(1, 9):
    numero = int(input(f'Informe o {num}º número: '))

    # Se o resto da divisão de um número por 2, for diferente de zero --> o número é impar.
    if numero % 2 != 0:
        soma += numero  # soma = soma + numero


# Mostra a soma
print(f'A soma dos números impares foi {soma}')

