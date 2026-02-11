
"""
Exemplo 14: Gráfico de barras (countplot)

Este exemplo mostra como criar gráficos de barras para variáveis qualitativas.
Necessário instalar os pacotes: pip install pandas matplotlib seaborn
Certifique-se de ter o arquivo titanic.xlsx na pasta principal.
Execute com: python 14_grafico_barras_countplot.py
"""


# Importa os pacotes pandas, matplotlib e seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lê o arquivo Excel 'titanic.xlsx'
arquivo_excel = 'titanic.xlsx'
titanic = pd.read_excel(arquivo_excel)

# Cria uma figura para o gráfico (ajustada para não exceder 1920x1080)
plt.figure(figsize=(12, 6), dpi=100)

# Cria um gráfico de barras para a variável 'sobreviveu'
sns.countplot(data=titanic, x='sobreviveu')
plt.title('Distribuição de Sobreviventes')
plt.xlabel('Sobreviveu')
plt.ylabel('Contagem')

# Exibe o gráfico
plt.tight_layout()
plt.show()
