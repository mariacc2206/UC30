import random

numeros = [45, 12, 78, 23, 56]
print("Lista oficial: ", numeros) 

numeros.sort()
print("Após sort(): ", numeros)

numeros.sort(reverse=True)
print("Após sort(): ", numeros)

dados = [1,2,3,4,5]
random.shuffle(dados)
print("Embaralhar: ", dados)
