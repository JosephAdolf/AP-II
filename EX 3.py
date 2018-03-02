n = int(input("Digite quantos números da série de Fibonacci você quer:"))
while n <= 0:
    n = int(input("Número inválido!!! Digite quantos números da série de Fibonacci você quer:"))
for i in range(1,n+1,1):
    if i <= 2:
        x=1
        y=1
        print(1,end=",")
    elif i > 2 and i != n:
        z=x+y
        print(z,end=",")
        y=x
        x=z
    else:
        z=x+y
        print(z)
        
# x = f n-1 y = f n-2 z = f n       
        
