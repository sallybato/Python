import pandas as pd

dados =pd.read_csv("dados.csv")

#informações básicas
print(dados.info())

#estatisticas descritivas
print(dados.describe())

#colunas e linhas
print(dados.columns)
print(len(dados))
