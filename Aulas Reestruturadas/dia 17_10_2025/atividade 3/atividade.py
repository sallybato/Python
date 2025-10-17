import pandas as pd
import matplotlib.pyplot as plt

alunos = pd.read_csv("alunos.csv")
notas = pd.read_csv("notas.csv")

#uso de merge para combinar os dados
dados_combinados = pd.merge(alunos,notas,on = "Matrícula")

#mostrando media de nota por curso
media = dados_combinados.groupby("Curso")["Nota"].mean()

#print(media)

#exibindografico de barras com essas médias
media.plot(kind="bar")
plt.title("Media de Notas por Curso")
plt.ylabel("Nota media")
plt.show()

#por ultimo, mostrar os cursos com media acima de 8.
