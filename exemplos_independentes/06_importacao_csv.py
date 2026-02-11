
"""
Exemplo 6: Importação de dados do CSV

Este exemplo mostra como importar um arquivo CSV com pandas.
Necessário instalar o pacote: pip install pandas
Certifique-se de ter o arquivo titanic.csv na pasta principal.
Execute com: python 06_importacao_csv.py
"""


# Importa o pacote pandas
import pandas as pd

# Lê o arquivo CSV 'titanic.csv' e armazena em um DataFrame
arquivo_csv = 'titanic.csv'
titanic = pd.read_csv(arquivo_csv, sep=',', decimal='.')

# Exibe as primeiras linhas do DataFrame
print('Primeiras linhas do dataset Titanic (CSV):')
print(titanic.head())
