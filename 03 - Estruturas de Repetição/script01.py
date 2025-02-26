# Escreva um algoritmo em Python que receba do usuário um nome, em seguida mostre letra por letra.

import time

nome = input('Informe um nome: ')

for x in nome:
    print(x)
    time.sleep(2)

