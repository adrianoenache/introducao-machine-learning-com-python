
"""
Exemplo 8: Remoção de variáveis em DataFrame

Este exemplo mostra como remover variáveis de um DataFrame.
Necessário instalar o pacote: pip install pandas
Certifique-se de ter o arquivo titanic.csv na pasta principal.
Execute com: python 08_remocao_variaveis.py
"""


# Importa o pacote pandas
import pandas as pd

# Lê o arquivo CSV 'titanic.csv'
arquivo_csv = 'titanic.csv'
titanic = pd.read_csv(arquivo_csv)

# Seleciona algumas colunas
colunas = ['sobreviveu', 'classe', 'sexo']
selecao_var = titanic[colunas]

# Remove a coluna 'classe' do DataFrame
selecao_var = selecao_var.drop(columns=['classe'])

print('Seleção após remoção da coluna "classe":')
print(selecao_var.head())
