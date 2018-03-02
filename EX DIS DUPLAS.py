n=-1
while n <=0:
    n=int(input("Digite quantos números você quer digitar:"))
ndiv=0
zsomado=0
for y in range (1,n+1,1):
    z= int(input("Digite um número:"))
    for i in range (1,z+1,1):
        resto = z%i
        if resto == 0:
            ndiv+=1
    if ndiv == 2:
        zsomado = zsomado + z
    ndiv = 0
print("A soma dos números primos é:",zsomado)
    


