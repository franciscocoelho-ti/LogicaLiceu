# Escreva um algoritmo em Python que leia dois números inteiros, correspondentes ao dividendo e ao divisor de uma divisão, e mostra o quociente. O algoritmo deve impedir que se efetue uma divisão por zero e imprimir uma mensagem de erro quando isso ocorrer.

# Entrada: Receber os dados do usuário
dividendo = int(input('Informe o dividendo: '))
divisor = int(input('Informe o divisor: '))

if divisor != 0:
    # Processamento: Gerar os dados/resultados
    quociente = dividendo / divisor

    # Saída: Exibir o(s) resultado(s)
    print('O resultado foi: ', quociente)
else:
    # Saída: Exibir o(s) resultado(s)
    print('Erro: Impossível dividir por zero.')




