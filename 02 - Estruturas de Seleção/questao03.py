# Uma cidade classifica um índice de poluição menor que 35 como agradável; de 35 até 60 desagradável e acima de 60 perigoso. Escreva um programa que lê um número real representando o índice de poluição e imprime a classificação adequada para ele.


# Entrada de Dados
indice = float( input('Informe o índice: ') )

if indice < 35:
    print('Indice está Agradável')
elif indice >= 35 and indice <= 60:
    print('Indice está Desagradável')
elif indice > 60:
    print('Indice está Perigoso')

    