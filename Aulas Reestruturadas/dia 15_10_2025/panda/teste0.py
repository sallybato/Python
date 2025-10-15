import pandas as pd

#lendo o arquivo CSV
dados = pd.read_csv("dados.csv")

#mostrando as 5 primeiras linhas
print(dados.head())
