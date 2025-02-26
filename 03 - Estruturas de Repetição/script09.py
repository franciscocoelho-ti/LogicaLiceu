# Um funcionário responsável pela expedição na Companhia C.I.A. tem o seguinte problema. O produto é muito frágil e deve ser enviado em caixas especiais. Essas caixas estão disponíveis em quatro tamanhos: extra-grande, grande, médio e pequeno, as quais podem conter até 50, 20, 5 e 1 unidade, respectivamente.
# Escreva um algoritmo em Python que leia a quantidade de produtos que deve ser enviada e imprima o número de caixas extra-grande, grande, média e pequena necessários para enviar os produtos utilizando o menor número de caixas e com a menor quantidade de espaço desperdiçado. A saída deve ser semelhante a seguinte:

# Caixa    Quant
# ------  ------
# Extra    211
# Grande   2
# Média    1
# Pequena  3

# -------------------------------------------------------------

# Variáveis para guardar a quantidade de caixas
caixa_extra = 0
caixa_grande = 0
caixa_medio = 0
caixa_pequena = 0

# Entrada de Dados: Receber a quantidade de produtos
quant_produtos = int(input('Informe a quant. de produtos: '))

# Repetir enquanto a quant, de produtos for igual a zero. Ou seja, enquanto tiver produto estou repetindo.
while quant_produtos != 0:
    if quant_produtos >= 50:
        caixa_extra = caixa_extra + 1           # Estou usando uma caixa extra
        quant_produtos = quant_produtos - 50    # Retirando 50 produtos da quantidade
    
    elif quant_produtos >= 20:
        caixa_grande = caixa_grande + 1         # Estou usando uma caixa grande
        quant_produtos = quant_produtos - 20    # Retirando 20 produtos da quantidade
    
    elif quant_produtos >= 5:
        caixa_medio = caixa_medio + 1           # Estou usando uma caixa média
        quant_produtos = quant_produtos - 5     # Retirando 5 produtos da quantidade
    
    elif quant_produtos >= 1:
        caixa_pequena = caixa_pequena + 1       # Estou usando uma caixa pequena
        quant_produtos = quant_produtos - 1     # Retirando 1 produtos da quantidade


# Exibir os resultados
print('Caixa    Quantidade')
print('-------------------')
print(f'Extra:   {caixa_extra}')
print(f'Grande:  {caixa_grande}')
print(f'Média:   {caixa_medio}')
print(f'Pequena: {caixa_pequena}')

