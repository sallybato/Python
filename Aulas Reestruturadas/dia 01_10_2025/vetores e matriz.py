#Criando listas (vetores)
#Vetor vazio
vetor = []
#vetor com valores
vetor = [10,20,30,40]
#Adicionais e removendo
vetor.append(50)#adiciona no fim
vetor.insert(2,15)#insere na posição 2
vetor.pop()#remove ultimo elemento
vetor.remove(20)#remove o valor 20

#criando uma matriz
matriz = [
    [1,2,3],
    [4,5,6]
]
#percorrendo matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
    
