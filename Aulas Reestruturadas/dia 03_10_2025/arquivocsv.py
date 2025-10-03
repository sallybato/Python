import csv             
#2 - Leia um arquivo CSV simples e mostre em formato de tabela
with open("dados.csv","r") as arq:
    conteudo =arq.read()
    print(conteudo)
