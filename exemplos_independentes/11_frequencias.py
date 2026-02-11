
"""
Exemplo 11: Estatísticas descritivas - tabela de frequências

Este exemplo mostra como calcular frequências de variáveis.
Necessário instalar o pacote: pip install pandas
Certifique-se de ter o arquivo titanic.csv na pasta principal.
Execute com: python 11_frequencias.py
"""


# Importa o pacote pandas
import pandas as pd

# Lê o arquivo CSV 'titanic.csv'
arquivo_csv = 'titanic.csv'
titanic = pd.read_csv(arquivo_csv)

# Calcula a frequência dos valores da coluna 'sobreviveu'
frequencia = titanic['sobreviveu'].value_counts()
print('Frequência absoluta da coluna "sobreviveu":')
print(frequencia)
print()

# Calcula a frequência relativa (percentual)
frequencia_relativa = titanic['sobreviveu'].value_counts(normalize=True)
print('Frequência relativa da coluna "sobreviveu":')
print(frequencia_relativa)
