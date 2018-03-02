def ePrimo():
    n = int(input("Digite um número:"))
    cont = 0
    for i in range (2,n):
        if n%i==0:
            cont +=1
    if cont != 0:
        return False
    else:
        return True
print(ePrimo())            
