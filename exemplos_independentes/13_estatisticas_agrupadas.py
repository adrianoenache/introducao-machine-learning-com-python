
"""
Exemplo 13: Estatísticas descritivas agrupadas

Este exemplo mostra como calcular estatísticas agrupadas por variáveis qualitativas.
Necessário instalar o pacote: pip install pandas
Certifique-se de ter o arquivo titanic.csv na pasta principal.
Execute com: python 13_estatisticas_agrupadas.py
"""


# Importa o pacote pandas
import pandas as pd

# Lê o arquivo CSV 'titanic.csv'
arquivo_csv = 'titanic.csv'
titanic = pd.read_csv(arquivo_csv)

# Valor médio da tarifa por classe
print('Valor médio da tarifa por classe:')
media_tarifa = titanic.groupby('classe')['valor_tarifa'].mean()
print(media_tarifa)
print()

# Percentual de sobreviventes por sexo
print('Percentual de sobreviventes por sexo:')
percentual_sobreviventes_sexo = titanic.groupby('sexo')['sobreviveu'].value_counts(normalize=True)
print(percentual_sobreviventes_sexo)
print()

# Percentual de sobreviventes por classe
print('Percentual de sobreviventes por classe:')
percentual_sobreviventes_classe = titanic.groupby('classe')['sobreviveu'].value_counts(normalize=True)
print(percentual_sobreviventes_classe)
