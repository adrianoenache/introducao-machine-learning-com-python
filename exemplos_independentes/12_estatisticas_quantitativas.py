
"""
Exemplo 12: Estatísticas descritivas - variável quantitativa

Este exemplo mostra como calcular estatísticas de variáveis numéricas.
Necessário instalar o pacote: pip install pandas
Certifique-se de ter o arquivo titanic.csv na pasta principal.
Execute com: python 12_estatisticas_quantitativas.py
"""


# Importa o pacote pandas
import pandas as pd

# Lê o arquivo CSV 'titanic.csv'
arquivo_csv = 'titanic.csv'
titanic = pd.read_csv(arquivo_csv)

idade = titanic['idade']

# Contagem de valores não nulos
print('Contagem de valores não nulos:')
print(idade.count())
print()

# Média aritmética
print('Média:')
print(idade.mean())
print()

# Mediana
print('Mediana:')
print(idade.median())
print()

# Valor máximo
print('Máximo:')
print(idade.max())
print()

# Valor mínimo
print('Mínimo:')
print(idade.min())
print()

# Primeiro quartil
print('Primeiro quartil (Q1):')
print(idade.quantile(q=0.25))
print()

# Terceiro quartil
print('Terceiro quartil (Q3):')
print(idade.quantile(q=0.75))
print()

# Variância
print('Variância:')
print(idade.var())
print()

# Desvio padrão
print('Desvio padrão:')
print(idade.std())
print()

# Estatísticas descritivas gerais
print('Estatísticas descritivas gerais:')
print(idade.describe())
