# Escreva um algoritmo em Python que leia as quatro notas de um aluno e calcula a média. O algoritmo deve imprimir a média calculada e uma mensagem indicando se o aluno foi aprovado, reprovado, ou se está de exame final. Um aluno é aprovado quando este obtém uma média maior ou igual a 6.0, e reprovado abaixo de 4.0.

# Entrada
nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
nota3 = float(input('Informe a 3ª nota: '))
nota4 = float(input('Informe a 4ª nota: '))

# Processamento
media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída
if media >= 6:
    print('O aluno está APROVADO com a média: ' + media)
elif media < 4:
    print('O aluno está REPROVADO com a média: ' + media)
else:
    print('O aluno está RECUPERAÇÃO com a média: ' + media)
