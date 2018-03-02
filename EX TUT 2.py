n=-1
while n <=0:
    n=int(input("Digite um inteiro e positivo:"))
ndiv=0
for i in range (1,n+1,1):
    resto = n%i
    if resto ==0:
        ndiv+=1
print("%d tem %d divisores" %(n,ndiv))
#For é melhor que o while nessa situação, pois temos já definido pelo número inserido pelo usuário quantos ciclos de repetição teremos que ter
