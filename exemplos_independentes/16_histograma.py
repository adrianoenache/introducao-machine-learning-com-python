
"""
Exemplo 16: Histograma

Este exemplo mostra como criar histogramas para variáveis métricas.
Necessário instalar os pacotes: pip install pandas matplotlib seaborn
Certifique-se de ter o arquivo titanic.xlsx na pasta principal.
Execute com: python 16_histograma.py
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

# Cria um histograma para a variável 'idade'
sns.histplot(data=titanic, x='idade', color='lightgreen', bins=20)
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')

# Exibe o gráfico
plt.tight_layout()
plt.show()
