#Funcoes de Calculo
def Celcius_to_Kelvin_Fahrenheit(Celcius):
    Fahrenheit = (Celcius * 1.8) + 32 
    Kelvin = Celcius + 273.15
    return Fahrenheit, Kelvin

def Fahrenheit_to_Celcius_Kelvin(Fahrenheit):
    Celcius = (Fahrenheit - 32) / 1.8
    Kelvin = (Fahrenheit - 32) * 5/9 + 273.15
    return Celcius, Kelvin

def Kelvin_to_Celcius_Fahrenheit(Kelvin):
    Celcius = Kelvin - 273.15 
    Fahrenheit = (Kelvin - 273.15) * 1.8 + 32
    return Celcius, Fahrenheit

#Comeco do programa
print("Bem vindo ao conversor de temperatura!")
print("--------------------------------------")

def Converter_Temperatura():
    continuar = True
    while (continuar):
        print("Escolha qual temperatura você quer converter:")
        print("(1) Celcius (2) Fahrenheit (3) Kelvin")
        
        #Erro
        try:
            temperatura = int(input("Digite o número da temperatura desejada: "))
            if (temperatura < 1 or temperatura > 3):
                print("Digite uma opção válida")
                print("--------------------------------------")
                continue

        except ValueError: 
            print("Digite um número válido")
            print("--------------------------------------")
            continue

        #Celcius
        if(temperatura == 1):
            print("--------------------------------------")
            Celcius = float(input("Digite a temperatura: "))
            Fahrenheit, Kelvin = Celcius_to_Kelvin_Fahrenheit(Celcius)
            print(f"A temperatura em Celcius é {Celcius:.2f}°C. A temperatura em Fahrenheit é {Fahrenheit:.2f}°F. A temperatura em Kelvin é {Kelvin:.2f}K.")
            print("--------------------------------------")

        #Fahrenheit
        elif(temperatura == 2):
            print("--------------------------------------")
            Fahrenheit = float(input("Digite a temperatura: "))
            Celcius, Kelvin = Fahrenheit_to_Celcius_Kelvin(Fahrenheit)
            print(f"A temperatura em Fahrenheit é {Fahrenheit:.2f}°F. A temperatura em Celcius é {Celcius:.2f}°C. A temperatura em Kelvin é {Kelvin:.2f}K.")
            print("--------------------------------------")


        #Kelvin
        elif(temperatura == 3):
            print("--------------------------------------")
            Kelvin = float(input("Digite a temperatura: "))
            Celcius, Fahrenheit = Kelvin_to_Celcius_Fahrenheit(Kelvin)
            print(f"A temperatura em Kelvin é {Kelvin:.2f}K. A temperatura em Celcius é {Celcius:.2f}°C. A temperatura em Fahrenheit é {Fahrenheit:.2f}°F")
            print("--------------------------------------")

        #Ver denovo -- Erro
        try:
            afirmacao = int(input("Deseja ver novamente? Digite 1 para Sim e 2 para Não: "))
            if afirmacao != 1:
                continuar = False

            elif (afirmacao == 1): 
                continuar == True
        except ValueError: 
            if (afirmacao < 1 or afirmacao >2):
                print("Digite um número ou opção válida")
                print("--------------------------------------")
                continue
Converter_Temperatura()