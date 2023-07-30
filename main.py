# Depósito, saque e extrato
import textwrap

def menu():
    menu = """\n
        ================ MENU ================
        [D]\tDepositar
        [S]\tSacar
        [E]\tExtrato
        [NC]\tNova conta
        [LC]\tListar contas
        [NU]\tNovo usuário
        [Q]\tSair
        => """
    return input(textwrap.dedent(menu))

def saque(novo_saque, saldo_total, valor_sacado, total_saques):
    if novo_saque > saldo_total:
        print("*Saldo insuficiente, por favor insira um valor menor ou igual ao saldo atual*\n")
    elif novo_saque > 500:
        print("*O valor é maior do que o limite permitido por saque, por favor insira um valor menor que 500 reais*\n")
    elif total_saques >= 3:
        print("*Você atingiu o número máximo de saques diários, tente novamente amanhã*\n")
    else:
        saldo_total -= novo_saque
        valor_sacado += novo_saque
        total_saques += 1
        print("\n*Saque realizado com sucesso!!*\n")
    
    return saldo_total, valor_sacado, total_saques

def deposito(novo_deposito, saldo_total, valor_deposito):
    if novo_deposito >= 0:
        saldo_total += novo_deposito
        valor_deposito += novo_deposito
        print("\n*Deposito realizado com sucesso*\n")
    
    return saldo_total, valor_deposito

def exibir_extrato(valor_deposito, valor_sacado, saldo_total):
    print(f"\nDeposito: R$ {valor_deposito:.2f}\n")
    print(f"Saque: R$ {valor_sacado:.2f}\n")
    print(f"Saldo: R$ {saldo_total:.2f}\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):

    for conta in contas:
        print(f"Agência:{conta['agencia']}\nC/C:{conta['numero_conta']}\nTitular:{conta['usuario']['nome']}")


def main():
    
    AGENCIA = "0001"

    msg_deposito = "Digite o valor que deseja depositar: "
    msg_saque = "Digite o valor que deseja sacar: "

    msg_extrato = ""

    valor_deposito = 0.0
    valor_sacado = 0.0
    saldo_total = 0.0
    total_saques = 0
    usuarios = []
    contas = []

    operacao = input(menu)

    while operacao != "Q":
        if operacao == "D":
            novo_deposito = float(input(f"{msg_deposito}"))
            saldo_total, valor_deposito = deposito(novo_deposito, saldo_total, valor_deposito)
        elif operacao == "S":
            novo_saque = float(input(f"{msg_saque}"))
            saldo_total, valor_sacado, total_saques = saque(novo_saque, saldo_total, valor_sacado, total_saques)
        elif operacao == "E":
           exibir_extrato(valor_deposito,  valor_sacado, saldo_total)
        elif operacao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif operacao == "NU":
            criar_usuario(usuarios)
        elif operacao == "LC":
            listar_contas(contas)
        else:
            print("\nPor favor insira um comando válido\n")

        operacao = input(menu)

    print("*Obrigado por usar o banco DIO!*")

main()