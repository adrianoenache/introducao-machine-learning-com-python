
"""
Exemplo 10: Limpeza de dados

Este exemplo mostra como remover valores ausentes e colunas.
Necessário instalar o pacote: pip install pandas
Certifique-se de ter o arquivo titanic.csv na pasta principal.
Execute com: python 10_limpeza_dados.py
"""


# Importa o pacote pandas
import pandas as pd

# Lê o arquivo CSV 'titanic.csv'
arquivo_csv = 'titanic.csv'
titanic = pd.read_csv(arquivo_csv)

# Remove todas as linhas com valores ausentes
titanic_limpo = titanic.dropna()
print('Dataset sem valores ausentes (NAs):')
print(titanic_limpo.head())
print()

# Remove a coluna 'nivel_cabine' e depois remove linhas com valores ausentes
titanic_sem_coluna = titanic.drop(columns=['nivel_cabine'])
titanic_limpo2 = titanic_sem_coluna.dropna()
print('Dataset sem coluna "nivel_cabine" e sem NAs:')
print(titanic_limpo2.head())
