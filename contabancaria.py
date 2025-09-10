
menu = True
saldo_conta = 0

while menu:
    print("======================")
    print("== Caixa Eletrônico ==")
    print("= 1. Depositar-------=")
    print("= 2. Sacar-----------=")
    print("= 3. Ver Saldo-------=")
    print("= 4. Sair -----------=")
    
    escolha = int(input("Selecione o que deseja executar:\n"))
    
    match escolha:
        case 1: 
            print("Você selecionou Depositar...")
            deposito = int(input("Insira o valor do deposito:\n"))
            saldo_conta = deposito
            print(f"O saldo atual da conta é >> {saldo_conta}")
        case 2:
            print("Você selecionou saque.")
            print(f"Seu saldo atual é: {saldo_conta}")
            saque = int(input("Insira o valor do saque:\n"))
            
            if saque > saldo_conta:
                print("valor de saque inválido, seu saldo é inferior ao valor do saque, tente novamente")
            else:
                saldo_conta = saldo_conta - saque
                print("Saque realizado com sucesso!")
        case 3:
            print(f"voce escolheu ver saldo! seu saldo atual é de : {saldo_conta}")            
        case 4:
            print("Saindo.. até") 
            menu = False   
        case _:
            print("Tentativa invalida, tente novamente por favot! :)")    
