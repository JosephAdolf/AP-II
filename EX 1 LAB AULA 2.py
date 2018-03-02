def ePrimo(n):
    cont = 0
    for i in range (2,n):
        if n%i==0:
            cont +=1
    if cont != 0 or n <=1:
        return False
    else:
        return True
n = int(input("Digite um número:"))
while n < 0:
    n = int(input("Número inválido!!! Digite um número:"))
print(ePrimo(n))            
