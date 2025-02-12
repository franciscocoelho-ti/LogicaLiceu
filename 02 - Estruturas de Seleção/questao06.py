# Para realizar o cálculo do Imposto de Renda a ser pago, é solicitado a renda anual e o número de dependentes do contribuinte. A renda líquida é calculada sobre a renda anual com um desconto de 2% para cada dependente do contribuinte. O contribuinte com uma renda líquida de até R$ 2.000,00 não paga imposto. Para aqueles que possuem renda líquida entre R$ 2.000,00 e R$ 5.000,00 o imposto é de 5% sobre o valor da renda líquida; e para rendas líquidas de R$ 5.000,00 até R$ 10.000,00 é de 10%. Rendas superiores a R$ 10.000,00 pagam 15% de imposto.


# Variáveis de Entrada
# Receber os valores: renda_anual (float) e numero_dependente (int)

renda_anual = float(input('Informe a renda anual: '))
numero_dependente = int(input('Informe o número de dependentes: '))

# Processamento
# Gerar a renda líquida
percentual_desconto = numero_dependente * 2
valor_desconto = (renda_anual / 100) * percentual_desconto
renda_liquida = renda_anual - valor_desconto

# Resultados
if renda_liquida <= 2000:
    print('Você não precisa pagar o Imposto de Renda')

elif renda_liquida > 2000 and renda_liquida <= 5000:
    valor_imposto = (renda_liquida / 100) * 5
    print('Valor do Imposto:', valor_imposto)

elif renda_liquida > 5000 and renda_liquida <= 10000:
    valor_imposto = (renda_liquida / 100) * 10
    print('Valor do Imposto:', valor_imposto)

else:
    valor_imposto = (renda_liquida / 100) * 15
    print('Valor do Imposto:', valor_imposto)
