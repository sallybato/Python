import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("alunos_notas.csv")
print(dados.head())
print(dados.describe())
print(dados.corr(numeric_only=True))

#dados["Nota"].hist()
#plt.title("Distribuição das Notas")
#plt.xlabel("Nota")
#plt.ylabel("Quantidade de Alunos")
#plt.show()

dados["Nota"].hist(bins=5,color="pink",edgecolor="black")
plt.title("Distribuição das Notas")
plt.xlabel("Faixas de Nota")
plt.ylabel("Quantidade de Alunos")
plt.show()

dados.boxplot(column="Nota")
plt.title("Boxplot das Notas")
plt.show()

plt.scatter(dados["Presenças"],dados["Nota"])
plt.title("Relação entre presença e nota")
plt.xlabel("Presenças (%)")
plt.ylabel("Nota")
plt.show()
