
"""
Exemplo 5: Importação de dados do Excel

Este exemplo mostra como importar um arquivo Excel com pandas.
Necessário instalar o pacote: pip install pandas
Certifique-se de ter o arquivo titanic.xlsx na pasta principal.
Execute com: python 05_importacao_excel.py
"""


# Importa o pacote pandas
import pandas as pd

# Lê o arquivo Excel 'titanic.xlsx' e armazena em um DataFrame
arquivo_excel = 'titanic.xlsx'
titanic = pd.read_excel(arquivo_excel)

# Exibe as primeiras linhas do DataFrame
print('Primeiras linhas do dataset Titanic (Excel):')
print(titanic.head())
