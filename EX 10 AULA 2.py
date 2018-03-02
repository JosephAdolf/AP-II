def Fibonacci(n):
   for i in range(1,n+1,1):
    if i <= 2:
        x=1
        y=1
    elif i > 2 and i != n:
        z=x+y
        y=x
        x=z
    else:
        z=x+y
        return z
def numero():
    n = int(input("Digite quantos números da série de Fibonacci você quer:"))
    while n <= 0:
        n = int(input("Número inválido!!! Digite quantos números da série de Fibonacci você quer:"))
    return Fibonacci (n)
print (numero())
