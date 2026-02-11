
"""
Exemplo 7: Seleção de variáveis em DataFrame

Este exemplo mostra como selecionar variáveis de um DataFrame.
Necessário instalar o pacote: pip install pandas
Certifique-se de ter o arquivo titanic.csv na pasta principal.
Execute com: python 07_selecao_variaveis.py
"""


# Importa o pacote pandas
import pandas as pd

# Lê o arquivo CSV 'titanic.csv'
arquivo_csv = 'titanic.csv'
titanic = pd.read_csv(arquivo_csv)

# Seleciona a coluna 'classe' do DataFrame
classe = titanic['classe']
print('Coluna "classe":')
print(classe.head())
print()

# Seleciona múltiplas colunas do DataFrame
colunas = ['sobreviveu', 'classe', 'sexo']
selecao_var = titanic[colunas]
print('Seleção de variáveis:')
print(selecao_var.head())
