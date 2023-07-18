menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
            valor = float (input("Informe o valor do depósito: "))

            if valor > 0 :
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print ("O valor foi depositado com sucesso")
    
            else :
                print ("Operação iválida! O valor informado não é válido")

    elif opcao == "2":
            valor = float (input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                  print ("Operação inválida! Não há saldo o suficiente para concluir a operação")

            elif excedeu_limite:
                  print ("Operação inválida! Valor de saque excedeu o valor de limite diário")

            elif excedeu_saques:
                  print ("Operação inválida! O número máximo de saques diários foi excedido")

            elif valor > 0:
                  saldo -= valor
                  extrato += f"Saque: R$ {valor:.2f}\n"
                  print ("Saque realizado com sucesso")
                  numero_saques += 1

            else:
                  print("Operação Inválida! O valor informado não é válido.")

    elif opcao == "3":
          print ("\n=============== EXTRATO =================")
          print ("Não houve realização de movimentações." if not extrato else extrato)
          print (f"\nSaldo: R$ {saldo:.2f}")
          print ("================================================================")

    elif opcao == "4":
          break
    
    else:
          print ("Operação selecionada inválida! Selecione uma nova operação")