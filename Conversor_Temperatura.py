print("Bem vindo ao conversor de temperatura!")
print("--------------------------------------")
continuar = True

while(continuar):
    print("Escolha qual temperatura você quer converter:")
    print("(1) Celcius (2) Fahrenheit (3) Kelvin")
    temperatura = int (input("Defina a temperatura: "))
    if(temperatura > 3):
        print("Digite uma temperatura válida.")
        print("--------------------------------------")
        continue

    if(temperatura == 1):
        print("--------------------------------------")
        Celcius = float (input("Digite a temperatura: "))
        
        Fahrenheit = (Celcius * 1.8) + 32 
        Kelvin = Celcius + 273.15
        
        print("A temperatura em Celcius é {}°C. A temperatura em Fahrenheit é {:.2f}°F. A temperatura em Kelvin é {:.2f}K.".format(Celcius, Fahrenheit, Kelvin))
        print("--------------------------------------")
        
    elif(temperatura == 2):
        print("--------------------------------------")
        Fahrenheit = float(input("Digite a temperatura: "))

        Celcius = (Fahrenheit - 32) / 1.8
        Kelvin = (Fahrenheit - 32) * 5/9 + 273.15

        print("A temperatura em Fahrenheit é {}°F. A temperatura em Celcius é {:.2f}°C. A temperatura em Kelvin é {:.2f}K.".format(Fahrenheit, Celcius, Kelvin))
        print("--------------------------------------")

    else:
        print("--------------------------------------")
        Kelvin = float(input("Digite a temperatura: "))

        Celcius = Kelvin - 273.15 
        Fahrenheit = (Kelvin - 273.15) * 1.8 + 32

        print("A temperatura em Kelvin é {}K. A temperatura em Celcius é {:.2f}°C. A temperatura em Fahrenheit é {:.2f}°F".format(Kelvin, Celcius, Fahrenheit))
        print("--------------------------------------")

    print("Deseja ver novamente? (1) Sim (2) Não")
    afirmacao = int (input("Digite 1 para Sim e 2 para Não: "))
    if (afirmacao.upper() > 2): 
        print("--------------------------------------")
        print("Digite um número válido")
        continue
    if (afirmacao.upper() == 1):
        print("--------------------------------------")
    elif(afirmacao.upper() == 2):
        break
        