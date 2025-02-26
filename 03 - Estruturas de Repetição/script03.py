# Escreva um algoritmo em Python que gera os números de 55 a 130, e exiba aqueles que divididos por 11 dão um resto igual a 5.


# Criar a repetição FOR para gerar o intervalo de 55 a 130, usando a função range()

for x in range(55,131):
    # Estrutura de Seleção
    if x % 11 == 5:
        print(x)


