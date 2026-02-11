
"""
Exemplo 4: Series com pandas

Este exemplo mostra como criar Series numéricas, de caracteres e lógicas.
Necessário instalar o pacote: pip install pandas
Execute com: python 04_series_pandas.py
"""


# Importa o pacote pandas
import pandas as pd

# Criação de uma Series numérica
numeros = pd.Series([10, 20, 30, 40, 50])
print('Series numérica:')
print(numeros)
print()

# Criação de uma Series de caracteres (texto)
cores = pd.Series(['Vermelho', 'Amarelo', 'Azul', 'Verde', 'Roxo'])
print('Series de caracteres:')
print(cores)
print()

# Criação de uma Series lógica (valores True/False)
logico = pd.Series([True, False, True, False, False])
print('Series lógica:')
print(logico)
