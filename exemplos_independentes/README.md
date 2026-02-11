
# Exemplos Independentes de Introdução ao Machine Learning com Python

Este diretório contém exemplos práticos e independentes para introdução ao uso de Python, NumPy, pandas, matplotlib e seaborn em tarefas comuns de análise de dados e visualização. Cada arquivo demonstra um conceito ou técnica específica, facilitando o aprendizado modular.

## Sumário dos Exemplos

| Arquivo | Descrição |
| ------- | --------- |
| 01_operacoes_basicas.py | Operações matemáticas básicas em Python (adição, subtração, multiplicação, divisão, exponenciação). |
| 02_numpy_funcao.py | Uso da função de raiz quadrada do NumPy. |
| 03_listas.py | Criação e manipulação de listas em Python. |
| 04_series_pandas.py | Criação de Series numéricas, de texto e lógicas com pandas. |
| 05_importacao_excel.py | Importação de dados de um arquivo Excel para um DataFrame pandas. |
| 06_importacao_csv.py | Importação de dados de um arquivo CSV para um DataFrame pandas. |
| 07_selecao_variaveis.py | Seleção de colunas (variáveis) em um DataFrame pandas. |
| 08_remocao_variaveis.py | Remoção de colunas (variáveis) de um DataFrame pandas. |
| 09_selecao_observacoes.py | Filtragem de linhas (observações) em um DataFrame com condições lógicas. |
| 10_limpeza_dados.py | Remoção de valores ausentes (NAs) e colunas de um DataFrame. |
| 11_frequencias.py | Cálculo de frequências absolutas e relativas de variáveis categóricas. |
| 12_estatisticas_quantitativas.py | Estatísticas descritivas para variáveis numéricas (contagem, média, mediana, quartis, variância, desvio padrão, etc). |
| 13_estatisticas_agrupadas.py | Estatísticas descritivas agrupadas por variáveis qualitativas (ex: média por classe, percentual de sobreviventes por sexo/classe). |
| 14_grafico_barras_countplot.py | Gráfico de barras (countplot) para variáveis qualitativas usando seaborn. |
| 15_grafico_barras_barplot.py | Gráfico de barras (barplot) para valores médios agrupados usando seaborn. |
| 16_histograma.py | Histograma para variáveis numéricas usando seaborn. |
| 17_scatterplot.py | Gráfico de dispersão (scatterplot) para duas variáveis numéricas. |
| 18_lineplot.py | Gráfico de linhas (lineplot) para valores médios agrupados. |
| 19_boxplot.py | Boxplot para análise de distribuição de variáveis numéricas. |

## Requisitos

- Python 3.x
- [NumPy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)

Instale os pacotes necessários com:

```bash
pip install numpy pandas matplotlib seaborn
```

## Observações

- Os exemplos que usam arquivos `titanic.csv` ou `titanic.xlsx` requerem que esses arquivos estejam na pasta principal do projeto.
- Para executar um exemplo, utilize:

  ```bash
  python exemplos_independentes/NOME_DO_ARQUIVO.py
  ```

- Cada script é independente e pode ser executado separadamente.

## Créditos

Material didático para minicurso de introdução ao Machine Learning com Python.
