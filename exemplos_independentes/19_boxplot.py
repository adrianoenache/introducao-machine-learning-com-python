
"""
Exemplo 19: Boxplot

Este exemplo mostra como criar boxplots para variáveis métricas.
Necessário instalar os pacotes: pip install pandas matplotlib seaborn
Certifique-se de ter o arquivo titanic.xlsx na pasta principal.
Execute com: python 19_boxplot.py
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

# Cria um boxplot para a variável 'idade'
sns.boxplot(y=titanic['idade'], color='orange')

# Calcula estatísticas para adicionar ao gráfico
minimo = titanic['idade'].min()
q1 = titanic['idade'].quantile(q=0.25)
q2 = titanic['idade'].median()
q3 = titanic['idade'].quantile(q=0.75)
maximo = titanic['idade'].max()

# Adiciona textos com os valores das estatísticas
plt.text(0, minimo, f'Mín = {minimo}', ha='center', va='top', fontweight='bold')
plt.text(0, q1, f'Q1 = {q1:.1f}', ha='center', va='top', fontweight='bold')
plt.text(0, q2, f'Q2 = {q2:.1f}', ha='center', va='center', fontweight='bold')
plt.text(0, q3, f'Q3 = {q3:.1f}', ha='center', va='bottom', fontweight='bold')
plt.text(0, maximo, f'Máx = {maximo}', ha='center', va='bottom', fontweight='bold')

# Adiciona título ao gráfico
plt.title('Boxplot da Idade', fontsize=20)
plt.ylabel('Idade', fontsize=15)
plt.xticks([])
plt.yticks(fontsize=14)

# Exibe o gráfico
plt.tight_layout()
plt.show()
