import textwrap

def menu():
    menu = """\n
    =============== MENU ===============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuário
    [5]\tNova Conta
    [6]\tListar contas
    [7]\tSair

    => """
    return input (textwrap.dedent(menu))

def depositar (saldo, valor, extrato, /):
   
    if valor > 0 :
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print ("O valor foi depositado com sucesso")
    
    else :
                print ("Operação iválida! O valor informado não é válido")
    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= limite_saques

            if excedeu_saldo:
                  print ("Operação inválida! Não há saldo o suficiente para concluir a operação")

            elif excedeu_limite:
                  print ("Operação inválida! Valor de saque excedeu o valor de limite diário")

            elif excedeu_saques:
                  print ("Operação inválida! O número máximo de saques diários foi excedido")

            elif valor > 0:
                  saldo -= valor
                  extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                  print ("Saque realizado com sucesso")
                  numero_saques += 1

            else:
                  print("Operação Inválida! O valor informado não é válido.")
            
            return saldo, extrato

def exibir_extrato (saldo, /, *, extrato):
          
          print ("\n=============== EXTRATO =================")
          print ("Não houve realização de movimentações." if not extrato else extrato)
          print (f"\nSaldo:\t\tR$ {saldo:.2f}")
          print ("================================================================")

def criar_usuario (usuarios):
    cpf = input("Insira somente os números de seu CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
            print("\n A operação não foi possível de ser realizada. O número de CPF já está cadastrado para um usuário!")
            return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço completo (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) 

    print ("Usuário cadastrado com sucesso")

def filtrar_usuarios (cpf, usuarios):
      usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
      return usuarios_filtrados [0] if usuarios_filtrados else None

def criar_conta (agencias, numero_conta, usuarios): 
      cpf = input("Insira o CPF do usuário: ")
      usuario = filtrar_usuarios(cpf, usuarios)

      if usuario:
            print("n\Sua conta foi registrada com sucesso")
            return {"agencias": agencias, "numero_conta": numero_conta, "usuario": usuario}
      
      print ("\n Operação não válida. Usuário não consta em cadastro.")
      return None

def listar_contas (contas):
      for conta in contas:
            linha = f"""\
                  Agência:\t{conta['agencias']}
                  C/C:\t\t{conta['numero_conta']}
                  Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

def main ():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float (input("Informe o valor do depósito: "))

            saldo, extrato = depositar (saldo, valor, extrato)

        elif opcao == "2":
            valor = float (input("Informe o valor do saque: "))

            saldo, extrato = sacar (
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas)  + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                  contas.append(conta)

        elif opcao == "6":
              listar_contas(contas)

        elif opcao == "7":
              break
        
        else:
              print ("Operação selecionada inválida! Selecione uma nova operação")

main()

