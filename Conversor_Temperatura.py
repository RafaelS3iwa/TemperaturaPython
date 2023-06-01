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
        print("Escolha qual temperatura você quer converter:\n" + "(1) Celcius \n" + "(2) Fahrenheit \n" + "(3) Kelvin")
        
        #Erro
        try:
            temperatura = int(input("Digite o número da temperatura desejada: "))
            if (temperatura < 1 or temperatura > 3):
                print("--------------------------------------")
                print("Digite uma opção válida")
                print("--------------------------------------")
                continue

        except ValueError:
            print("--------------------------------------") 
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

        #Ver denovo
        while True:
            afirmacao = input("Deseja ver novamente? Digite: \n" + "(1) para Sim \n" + "(2) para Não\n" + "Opção: ")
            if afirmacao == '1':
                break
            elif afirmacao == '2':
                continuar = False
                break
            else:
                print("--------------------------------------")
                print("Digite uma opção válida (1 para Sim ou 2 para Não)")
                print("--------------------------------------")

Converter_Temperatura()