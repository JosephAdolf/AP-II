fim = 0
maior = 0
menor = 0
while fim >= 0:
    n = int(input("Digite um número:"))
    if n < 0:
        fim -= 1
    elif n >= maior:
        maior = n
    elif n <= menor:
        menor = n
print("Número Maior:",maior,"Número Menor:",menor)
    
