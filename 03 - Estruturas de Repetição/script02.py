# Escreva um algoritmo em Python que receba do usuário um nome, e mostre ao final quantas vogais tem no nome informado.

nome = str.lower(input('Informe um nome: '))
quant_vogais = 0

for x in nome:
    if x in 'aeiou':
        quant_vogais = quant_vogais + 1

print('Total de vogais:', quant_vogais)

