soma = 0
lista = []
tamanho = int(input("Digite a quantidade de números que você quer adicionar a lista:"))
for i in range (0,tamanho):
    entrada = int(input("Digite um número:"))
    lista.append(entrada)
    print("Número adicionado!!")
for j in range (0,tamanho):
    soma+=lista[j]
print("A soma é:",soma)
