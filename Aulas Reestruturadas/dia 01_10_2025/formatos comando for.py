#Formatos do comando FOR
# DE 0 ATÉ 4
for i in range (5):
    print(i)

#de 2 ate 6
for i in range (2,6):
    print(i)
#de 10 até 0, de -2 em -2
for i in range (10, -1, -2):
    print(i)

#percorrendo listas
frutas = ["maçã", "banana","uva"]
for i in frutas:
    print(i)

#percorrendo strings
for letra in "Python":
    print(letra)

#percorrendo tuplas
 numeros = (10,20,30)
 for i in numeros:
     print(i)

#percorrendo dicionarios
 pessoa = {"nome": "Lambarildo", "idade": 23, "cidade": "Recife"}

 for i in pessoa:
     print(i)
 for i, j in pessoa,items():
     print(i,"->", j)

#for com enumerate()
nomes = ["ana", "Bruno", "Carlos"]
for i, nome in enumerate(nomes):
    print(i,nome)

#for com zip() percorre duas (ou mais) listas ao mesmo tempo
 alunos = ["ana", "Bruno", "Carlos"]
 notas = [8,9,7]
 for aluno, nota in zip(alunos,notas):
     print(aluno,"tirou",nota)


     
