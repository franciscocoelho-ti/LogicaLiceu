# Um número inteiro é primo se é divisível por 1 e por ele mesmo. Escreva um algoritmo em Python que verifique se um número inteiro fornecido pelo teclado é primo.

numero = int(input('Informe um número: '))
contador = 1
quantDivisao = 0

while contador <= numero:
    if numero % contador == 0:
        quantDivisao += 1
    # incrementar o contador
    contador += 1

# Resultado
if quantDivisao == 2:
    print('O número informado É PRIMO')
else:
    print('O número informado NÃO É PRIMO')
