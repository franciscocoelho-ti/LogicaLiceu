# Funções
# Bloco de código (independente), executa a partir de uma chamada.
# Criar -->  Chamar
# Declaração de uma função no Python é feita pela comando "def"

# Dentro de funções não se deve utilizar as função input() e print()# O parâmetro substitui os input()
# O retorno substitui os print()



def somar(numero_1, numero_2, *args):
    '''
        Autor: Francisco Coelho <franciscocoelho.ti@gmail.com>
        Nome da Função: somar
        Parâmetro: numero_1 -> int, numero_2 -> int
        Retorno: numero_1 + numero_2 -> int
    '''
    resultado = numero_1 + numero_2
    return resultado
    
print(somar(20, 45, 19, 40))


