int(input("Digite o primeiro número"))
int(input("Digite o segundo número"))

def soma_segura(a, b):
    try:
        return a + b  
    except TypeError: 
        print("Entrada Invalida")
    