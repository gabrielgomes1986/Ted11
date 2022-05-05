#Consutra uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:

import random

matriz_10x10a = []

for i in range(10):
    
    matriz_aux = []
    
    for j in range(10):    
        matriz_aux.append(random.randint(0, 100))
    
    matriz_10x10a.append(matriz_aux)        


for linha in matriz_10x10a:
    print(linha)
    
print('*' * 100)
    
resultado_soma = 0

for l in matriz_10x10a:
    
    for c in l:
        
        resultado_soma += c

print(f'A soma é = {resultado_soma}')

matriz_10x10b = []

for l in range(0, len(matriz_10x10a)):
    
    lista_auxiliar = []
    
    for c in range(0, len(matriz_10x10a[l])):
        
        resultado_multiplicacao = matriz_10x10a[l][c] * 3
        lista_auxiliar.append(resultado_multiplicacao)
        
    matriz_10x10b.append(lista_auxiliar)
        
print(matriz_10x10b)