#Sistema bancario de saque, deposito e consulta de saldo


saldo = 0

while True:

    print("\nSelecione uma opção:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Saldo atual")
    print("4 - Sair")

    opcoes = int(input("Opção: "))

    if opcoes == 1:
        deposito = int(input("Valor que deseja depositar: "))
        saldo += deposito
        print("Valor adicionado com sucesso")

    if opcoes == 2:
        saque = int(input("Valor que deseja sacar: "))
        if saque <= saldo:
            saldo -= saque
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")


    if opcoes == 3:
        print("Seu saldo é:", saldo)

    if opcoes == 4:
        print("Sistema Encerrado")
        break
