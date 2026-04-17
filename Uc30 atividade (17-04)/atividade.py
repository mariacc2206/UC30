#Questão 1 
print("Helo, word!")



#Questão 2
idade = int(input("Digite sua idade:"))

if idade >= 16:
    print(" Você pode votar.")
else: 
    print("Você não pode votar.")



#Questão 3
total = 0

while True:
    valor = float(input("Digite o valor de cada item (0 para parar): "))
    if valor == 0:
        break
    total = valor

print(" Valor total da compra:", total)  



#Questão 4
#não sei 

#questão 5
amigos = ["Bola 8", "Arthur", "Lydia", "Fabiany"]

quantidade = 4
if quantidade == 4:
   print("É par!")
else: 
    print("Não é par!")


#Questão 9
notas = [3, 8,5, 10, 4, 9]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print("Quantidade acima de 7:", contador)








