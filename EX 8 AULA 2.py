def fatorial (n):
    multi = n
    if n == 0:
        return ("0! = 1")
    for i in range (n,0,-1):
        if n != i: 
            multi *= i
    return multi 
def numero():
    n = int(input("Digite um número:"))
    while n < 0:
        n = int(input("Número negativo não é válido!! Digite um número:"))
    return fatorial (n)
print (numero())
