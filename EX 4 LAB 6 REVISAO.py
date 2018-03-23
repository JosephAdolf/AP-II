def comp_palavra(palavra,letra,tamanho):
    if tamanho == 0:
        if palavra[0].upper() == letra.upper():
            return 1
        else:
            return 0
    if palavra[tamanho].upper() == letra.upper():
        return 1 + comp_palavra(palavra,letra,tamanho-1)
    else:
        return 0 + comp_palavra(palavra,letra,tamanho-1)
        
        








letra = input("Digite a letra que você quer comparar:")
palavra  = input("Digite a palavra que você quer comparar:")
tamanho = len(palavra)-1
print("A letra",letra,"aparece",comp_palavra(palavra,letra,tamanho),"vezes!!")
