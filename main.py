# Depósito, saque e extrato

menu = '''##### Bem-vindo ao banco da DIO #####

    [D] Deposito
    [S] Saque
    [E] Extrato
    [Q] Sair
    
    Selecione uma das opcoes acima: 
'''

msg_deposito = "Digite o valor que deseja depositar: "
msg_saque = "Digite o valor que deseja sacar: "

msg_extrato = ""

valor_deposito = 0.0
valor_sacado = 0.0
saldo_total = 0.0
total_saques = 0

operacao = input(menu)

while operacao != "Q":
    if operacao == "D":
        novo_deposito = float(input(f"{msg_deposito}"))
        if novo_deposito >= 0:
            saldo_total += novo_deposito
            valor_deposito += novo_deposito
            print("\n*Deposito realizado com sucesso*\n")
    elif operacao == "S":
        novo_saque = float(input(f"{msg_saque}"))
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
    elif operacao == "E":
        print(f"\nDeposito: R$ {valor_deposito:.2f}\n")
        print(f"Saque: R$ {valor_sacado:.2f}\n")
        print(f"Saldo: R$ {saldo_total:.2f}\n")
    else:
        print("\nPor favor insira um comando válido\n")

    operacao = input(menu)

print("*Obrigado por usar o banco DIO!*")

