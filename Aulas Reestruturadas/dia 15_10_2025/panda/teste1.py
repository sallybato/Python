import pandas as pd

#lendo o arquivo CSV
dados = pd.read_csv("dados.csv")

#filtrar apenas alunos de Computação
comp = dados[dados["Curso"] == "Computação"]
print(comp)

#ordenar por nota(decrescente)
ordenado = dados.sort_values(by="Nota", ascending=False)
print(ordenado)

#ordenar por Idade(decrescente)
ordenado1 = dados.sort_values(by="Idade", ascending=False)
print(ordenado1)
