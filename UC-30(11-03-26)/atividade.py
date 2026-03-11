notas = {}

notas["nome"] = input("Qual o seu nome:")
notas["nota1"] = float(input("nota 1° prova:"))
notas["nota2"] = float(input("nota 2° prova:"))

media = (notas["nota2"] + notas["nota1"]) /2
notas["media"] = media 

if notas["media"] >=7:
    print(f"Você foi aprovado.Sua media foi de{media}")
elif notas["media"] >=5:
    print("Você está de recuperação!")
else:
    print("Você foi aprovado!")

print("\n Dados")
print("Nome: ", notas["nome"])
print("Nota1: ", notas["nota1"])
print("nota2: ", notas["nota2"]) 
print("media: ", round(notas["media"], 2))