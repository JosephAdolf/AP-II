def somaDigitos (n):
    y = len(n)
    z = 0
    for i in range (0,y,1):
        z += int(n[i])
    return z
def numero():
    n = input("Digite o número positivo:")
    a = int(n)
    while a < 0:
        n = input("Número negativo !! Digite o número positivo:")
        a = int(n)     
    return  somaDigitos (n)
print (numero())
