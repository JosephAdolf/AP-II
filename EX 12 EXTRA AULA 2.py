def mdc (x1,x2):
    if x1%x2 == 0:
        print("MDC = ",x2)
        return
    elif x2%x1 == 0:
        print("MDC = ",x1)
        return
    else:
        if x1 > x2:
            maior = x1
        else:
            maior = x2
        for i in range (1,maior+1):
            if x1%i == 0 and x2%i == 0:
                divisor = i
        print ("MDC = ",divisor)
        return
        
def entrada ():
    x1 = int(input("Digite um número:"))
    x2 = int(input("Digite outro número:"))
    mdc (x1,x2)
entrada()
