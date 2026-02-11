
"""
Exemplo 17: Gráfico de pontos (scatterplot)

Este exemplo mostra como criar gráficos de dispersão para variáveis métricas.
Necessário instalar os pacotes: pip install pandas matplotlib seaborn
Certifique-se de ter o arquivo titanic.xlsx na pasta principal.
Execute com: python 17_scatterplot.py
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

# Cria um gráfico de dispersão para passageiros com tarifa < 100
filtro_tarifa = titanic['valor_tarifa'] < 100
sns.scatterplot(data=titanic[filtro_tarifa], x='idade', y='valor_tarifa')
plt.title('Dispersão: Idade x Valor da Tarifa (tarifa < 100)')
plt.xlabel('Idade')
plt.ylabel('Valor da Tarifa')

# Exibe o gráfico
plt.tight_layout()
plt.show()
