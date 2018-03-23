cont = 0
letra = input("Digite a letra que você quer comparar:")
palavra  = input("Digite a palavra que você quer comparar:")
for i in range (0,len(palavra)):
    if palavra[i].upper() == letra.upper():
        cont += 1
print("A letra",letra,"aparece",cont,"vezes!!")
                 
