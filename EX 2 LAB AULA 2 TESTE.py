def ePrimo(n):
    cont = 0
    for i in range (2,n):
        if n%i==0:
            cont +=1
    if cont != 0 or n <=1:
        return False
    else:
        return True
    
def somaPrimo(qtd):
    soma = 0
    for y in range(qtd):
        n = int(input("Digite um número:"))
        while n < 0:
            n = int(input("Número inválido!!! Digite um número:"))
        if ePrimo(n) == True:
            soma += n
    return soma

qtd = int(input("Quantos números você quer colocar?:"))
while qtd < 0:
    qtd = int(input("Número inválido!!! Quantos números você quer colocar?:"))
print(somaPrimo(qtd))            

