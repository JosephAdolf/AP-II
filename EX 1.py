n = int(input("Digite um número:"))
while n < 0:
    n = int(input("Número negativo não é válido!! Digite um número:"))
multi = n
if n == 0:
    print ("0! = 1")
elif n == 1:
    print ("1! = 1")
else:
    print(n,"! =",end="")
    for i in range (n,0,-1):
        if n != i: 
            multi *= i
        if i != 1:
            print(i,end=" x ")
        else:
            print(i,"=",multi)
    
    
    
