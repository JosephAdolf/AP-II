def mmc (x1,x2):
    if x1 < x2:
        menor = x1
    else:
        menor = x2
    if x1%x2 == 0 or x2%x1 == 0:
        print("MMC = ",menor)
        return
    else:
        while True:
            if menor%x1 == 0 and menor%x2 == 0:
                print("MMC = ",menor)
                break
            else:
                menor += 1
def entrada ():
    x1 = int(input("Digite um número:"))
    x2 = int(input("Digite outro número:"))
    mmc (x1,x2)
entrada()

