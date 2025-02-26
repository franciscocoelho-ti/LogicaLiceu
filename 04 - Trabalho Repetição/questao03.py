# Em uma competição de ginástica olímpica a nota é determinada por um painel de seis juízes. Cada um dos juízes atribui uma nota entre zero e dez para o desempenho do atleta. Para calcular a nota final, a nota mais alta e a nota mais baixa são descartadas e é calculado a média das quatro restantes. Escreva um algoritmo em Python que leia 6 notas entre zero e dez e calcule a média após o descarte da maior e da menor nota.

menor_nota = None
maior_nota = None
soma_notas = 0
contador = 1

for cont in range(6):
    nota = float(input('Informe nota: '))
    soma_notas += nota

    if contador == 1:
        menor_nota = nota
        maior_nota = nota
        contador += 1
    else:
        if nota < menor_nota:
            menor_nota = nota
        elif nota > maior_nota:
            maior_nota = nota
    
# Removendo a menor e maior nota do somatório
soma_notas = soma_notas - (maior_nota + menor_nota)

# Fazendo a média das 4 notas restantes
soma_notas /= 4 

# Exibindo a média final do atleta
print(f'A média do(a) atleta foi: {soma_notas}')

