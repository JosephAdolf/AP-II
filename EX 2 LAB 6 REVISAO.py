def soma_lista(x,y):
    if y == 0:
        return lista[0]
    return lista[y] + soma_lista(x,y-1)





lista = []
tamanho = int(input("Digite a quantidade de números que você quer adicionar a lista:"))
for i in range (0,tamanho):
    entrada = int(input("Digite um número:"))
    lista.append(entrada)
    print("Número adicionado!!")

print("A soma é:",soma_lista(lista,tamanho-1))
