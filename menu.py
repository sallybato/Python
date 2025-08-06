while True:
    print("------------------------")
    print("1. Somar ---------------")
    print("2. Multiplicar ---------")
    print("3. Dividir -------------")
    print("4. Subtrair ------------")
    print("------------------------")

    escolha = int(input("Digite o numero da sua escolha de operações:\n"))

    match escolha:
        case 1:
            print("----------------------------")
            print("  Você selecionou Somar    !")
            print("----------------------------")
            print("\n")
            valor1 = int(input("Insira o primeiro valor:"))
            valor2 = int(input("Insira o segundo valor:"))

            soma = valor1 + valor2

            print("A soma dos seus dois numeros inseridos é: \n",soma)

        case 2:
            print("----------------------------")
            print("Você selecionou Multiplicar!")
            print("----------------------------")
            print("\n")
            valor1 = int(input("Insira o primeiro valor:"))
            valor2 = int(input("Insira o segundo valor:"))

            multiplica = valor1 * valor2

            print("A multiplicação dos dois numeros inseridos é: \n",multiplica)

        case 3:
            print("----------------------------")
            print("  Você selecionou Dividir!  ")
            print("----------------------------")
            print("\n")
            valor1 = int(input("Insira o primeiro valor:"))
            valor2 = int(input("Insira o segundo valor:"))

            dividir = valor1/valor2
            print("A divisão dos dois numeros inseridos é: \n",dividir)

        case 4:
            print("----------------------------")
            print("  Você selecionou Subtrair! ")
            print("----------------------------")
            print("\n")    
            valor1 = int(input("Insira o primeiro valor:"))
            valor2 = int(input("Insira o segundo valor:"))

            subtrair = valor1 - valor2
            print("A subtração dos dois numeros inseridos é: \n",subtrair)

        case _:
            print("Opção inválida! Por favor escolha um numero de 1 a 4.")
