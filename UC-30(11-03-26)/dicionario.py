
contato = {
    "@camila": 1.66,
    "@paola": 1.80,
    "@sheron": 1.80,
    "@bruna": 1.60,
    "@joao": 1.70
}

#obter chaves 
print("Chaves: ")
for insta in contato.keys():
    print(insta)

#obter valores
print("\n valores")
for nome in contato.values():
    print(nome)

    print("\n pares: ") #obter pares (chaves-valor)
    for insta, nome in contato.items():
        print(f"{insta} --> {nome}")

# Ordenar por chave
print("Ordenar por chave: ")
for insta in sorted(contato.keys()):
    print(f"{insta} --> {contato[insta]:.2f}m")

#ordenar por valor 
from operator import itemgetter
print("\n ordenado por valor (altura): ")
for insta, estatura in sorted(contato.items())