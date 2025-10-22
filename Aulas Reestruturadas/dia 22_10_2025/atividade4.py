import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("registro.csv")

minmaxnotas = dados.groupby("Curso")["Nota"].agg(['min','max'])
print("=" *45)
print(minmaxnotas) 
#agrupa notas por grupo (Curso)
print("=" *45)
media_geral = dados["Nota"].mean()
print(f"Media geral de Notas: {media_geral: .2f}")
print("="*45)
alunos_acima_media = dados[dados["Nota"]> media_geral]
#indexação booleana para filtragem

quantidade_alunos = alunos_acima_media.shape[0]

print(f"Quantos alunos tem nota acima da média geral: {quantidade_alunos}")
print("="*45)
print(f"Alunos acima da media:\n {alunos_acima_media}")
print("="*45)

proporcao = dados.groupby("Curso")["Nome"].nunique().sort_values(ascending=False)
total_alunos = proporcao.sum()
proporcao_percentual = (proporcao/total_alunos)*100

proporcao.plot.pie(
    figsize=(9, 9), #tamanho do gráfico
    autopct='%1.0f%%', #coloca porcentagem dentro da pizza
    startangle=90, #faz a pizza começar de cima
    ylabel = '' #remove o rótulo Nome ou similar do eixo Y
)

plt.title('Proporção de alunos por Curso')
plt.axis('equal')  #garante que o circulo nao fique oval
plt.show()
