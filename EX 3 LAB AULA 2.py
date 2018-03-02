def exibeMsg():
    print("Esse programa converte faixas de temperaturas em Fahrenheit para Celsius (ou Celsius para Fahrenheit)"
          "\nPara converter de Fahrenheit para Celsius digite F; Para converter de Celsius para Fahrenheit digite C")
def getConvertTo():
    pedido = input("Digite F ou C:")
    return pedido
def exibeCelsiusTOFahrenheit(start, end):
    f = (1.8*(end-start)) + 32
    print(f)
def exibeFahrenheitTOCelsius(start, end):
    c = ((end-start)-32)/1.8
    print(c)
exibeMsg()
pedido = getConvertTo()
while pedido.upper() != "C" and pedido.upper() != "F":
    pedido = getConvertTo()
if pedido.upper() == "C":
    x = float(input("Digite a temperatura inicial em Celsius:"))
    y = float(input("Digite a temperatura final em Celsius:"))
    exibeCelsiusTOFahrenheit(x,y)
elif pedido.upper() == "F":
    x = float(input("Digite a temperatura inicial em Fahrenheit:"))
    y = float(input("Digite a temperatura final em Fahrenheit:"))
    exibeFahrenheitTOCelsius(x,y)
