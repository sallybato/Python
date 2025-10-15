import pandas as pd
import matplotlib.pyplot as plt

#lendo o arquivo CSV
dados = pd.read_csv("dados.csv")

#=== HISTORICO DE NOTAS ===
dados["Nota"].hist()
plt.title("Distribuição das Notas")
plt.xlabel("Nota")
plt.xlabel("Quantidade de Alunos")
plt.show()

# === CALCULAR MÉDIA DE NOTAS POR CURSO ===
media_por_curso = dados.groupby("Curso"["Nota"].mean())
print(media_por_curso)

# === GRAFICO DE BARRAS DA MEDIA POR CURSO ===
media_por_curso.plot(kind="bar")
plt.title("Media de Notas por Curso")
plt.ylabel("Nota media")
plt.show()
