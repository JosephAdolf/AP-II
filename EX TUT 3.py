n=-1
while n <=0:
    n=int(input("Digite um inteiro e positivo:"))
ndiv=0
for i in range (1,n+1,1):
    resto = n%i
    if resto ==0:
        ndiv+=1
if ndiv == 2:
    print("É Número Primo!!!")
else:
    print("Não é Número Primo!!!")

