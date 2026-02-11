
"""
Exemplo 18: Gráfico de linhas (lineplot)

Este exemplo mostra como criar gráficos de linhas para valores médios.
Necessário instalar os pacotes: pip install pandas matplotlib seaborn
Certifique-se de ter o arquivo titanic.xlsx na pasta principal.
Execute com: python 18_lineplot.py
"""


# Importa os pacotes pandas, matplotlib e seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lê o arquivo Excel 'titanic.xlsx'
arquivo_excel = 'titanic.xlsx'
titanic = pd.read_excel(arquivo_excel)

# Agrupa os dados por classe e calcula a média da tarifa
dados_linha = titanic.groupby('classe')['valor_tarifa'].mean().reset_index()

# Cria uma figura para o gráfico (ajustada para não exceder 1920x1080)
plt.figure(figsize=(12, 6), dpi=100)

# Cria um gráfico de linhas para a tarifa média por classe
sns.lineplot(data=dados_linha, x='classe', y='valor_tarifa', marker='o', linewidth=3, color='purple')

# Adiciona título e rótulos
plt.title('Tarifa Média por Classe - Titanic', fontsize=20)
plt.xlabel('Classe', fontsize=15)
plt.ylabel('Tarifa Média', fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Exibe o gráfico
plt.tight_layout()
plt.show()
