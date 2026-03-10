#sem dicionario
matricula1 = 2026001
nome1 = "Ana Silva"
telefone1 = "9999-8888"

#com dicionário
aluno = {
    "matricula": 2026001,
    "nome": "Ana Silva",
    "telefone": "9999-8888"
}

print(aluno)

contato = {
    "@camila": "Camila",
    "@paola": "paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
    "@Joao": "João",

}

print(contato)
print(type(contato))

#acesso direto ao dicionário
print(contato["@camila"])

#acesso seguro com get()
print(contato.get("@paola"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))

print("Original: ", contato) #acessondo a lista original

#add novo elemento
contato["@giovanna"] = "Giovanna"
print("Após add: ", contato)

contato.update({
    "@bruna": "Bruna Marquezine",
    "@camila": "Camila Q.+"
})

print("Após atualização: ", contato)

#pop: remove e retorna
removido = contato.pop("@sheron")
print(f"Removido: {removido}")
print("Após o del: ", contato)

# del remove sem retornar
del contato["@paola"]
print("Após o del: ", contato)

#clear esvazia tudo 
copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("Cópia: ", copia)

print("Números de contato: ", len(contato))

contato.pop("@camila")
print("Após remover um: ", len(contato))

#verificar existência
if "@inexistente" in contato:
    print("Existente")
else:
    print("Não existe.")

#verificar
#Dicionário Vazio

vazio = {}

#Dicionário com tipos mistos 
dados = {
    "nome": "João",
    "idade": 25,
    "altura": 1.79,
    "ativo": true 
}

print

("Vazio: ", vazio)
("Vazio: ", dados)