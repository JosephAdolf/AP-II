x = int(input("Digite um número:"))
y = int(input("Digite outro número:"))
z = int(input("Digite outro número:"))
if x <= y and x <= z:
    print(x)
elif y <= x and y <= z:
    print(y)
else:
    print(z)
