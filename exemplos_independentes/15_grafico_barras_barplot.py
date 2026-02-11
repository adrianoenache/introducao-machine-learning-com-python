
"""
Exemplo 15: Gráfico de barras geral (barplot)

Este exemplo mostra como criar gráficos de barras para valores médios.
Necessário instalar os pacotes: pip install pandas matplotlib seaborn
Certifique-se de ter o arquivo titanic.xlsx na pasta principal.
Execute com: python 15_grafico_barras_barplot.py
"""


# Importa os pacotes pandas, matplotlib e seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lê o arquivo Excel 'titanic.xlsx'
arquivo_excel = 'titanic.xlsx'
titanic = pd.read_excel(arquivo_excel)

# Agrupa os dados por cidade de embarque e calcula a média da tarifa
dados = titanic.groupby('embarque')['valor_tarifa'].mean().reset_index()

# Cria uma figura para o gráfico (ajustada para não exceder 1920x1080)
plt.figure(figsize=(12, 6), dpi=100)

# Cria um gráfico de barras para o valor médio da tarifa
ax1 = sns.barplot(data=dados, x='embarque', y='valor_tarifa', palette='bright')

# Adiciona os valores das barras
for container in ax1.containers:
	ax1.bar_label(container, fmt='%.2f', padding=3, fontsize=12)

# Adiciona título e rótulos
plt.title('Tarifa Média', fontsize=20)
plt.xlabel('Cidade de Embarque', fontsize=15)
plt.ylabel('Valor', fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Exibe o gráfico
plt.tight_layout()
plt.show()
