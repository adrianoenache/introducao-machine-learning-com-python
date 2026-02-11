
"""
Exemplo 9: Seleção de observações (filtros)

Este exemplo mostra como filtrar observações usando condições.
Necessário instalar o pacote: pip install pandas
Certifique-se de ter o arquivo titanic.csv na pasta principal.
Execute com: python 09_selecao_observacoes.py
"""


# Importa o pacote pandas
import pandas as pd

# Lê o arquivo CSV 'titanic.csv'
arquivo_csv = 'titanic.csv'
titanic = pd.read_csv(arquivo_csv)

# Filtra sobreviventes
filtro_sobreviventes = titanic['sobreviveu'] == 'sim'
sobreviveu = titanic[filtro_sobreviventes]
print('Sobreviventes:')
print(sobreviveu.head())
print()

# Filtra adultos do sexo masculino
filtro_masc_adultos = (titanic['sexo'] == 'masculino') & (titanic['idade'] >= 18)
masc_adultos = titanic[filtro_masc_adultos]
print('Adultos masculinos:')
print(masc_adultos.head())
print()

# Filtra mulheres ou crianças
filtro_mulheres_criancas = (titanic['sexo'] == 'feminino') | (titanic['idade'] < 18)
mulheres_criancas = titanic[filtro_mulheres_criancas]
print('Mulheres ou crianças:')
print(mulheres_criancas.head())
