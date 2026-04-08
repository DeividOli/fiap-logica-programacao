#Fazer o usuário escolher o tipo de investimento
while True:
    tipoInvestimento = int(input("Opções:\n1. CDB \n2. LCI \n3. LCA: \nEscolha o tipo de investimento: "))
    if tipoInvestimento == 1 or tipoInvestimento == 2 or tipoInvestimento == 3:
        break
    else:
        print("Digite uma opcao valida!")

valorResgatado = float(input("Digite o valor a ser resgatado: "))
diasInvestidos = int(input("Digite o numero de dias que o valor permaneceu investido: "))
aliquota_180dias = 22.5
aliquota_360dias = 20
aliquota_720dias = 17.5
aliquotaMais720 = 15

if tipoInvestimento == 1 and diasInvestidos <= 180:
    print(F"O valor do imposto de renda a ser pago é R$: {valorResgatado / 100 * aliquota_180dias:.2f}")
elif tipoInvestimento == 1 and diasInvestidos <= 360:
    print(F"O valor do imposto de renda a ser pago é R$: {valorResgatado / 100 * aliquota_360dias:.2f}")
elif tipoInvestimento == 1 and diasInvestidos <= 720:
    print(F"O valor do imposto de renda a ser pago é R$: {valorResgatado / 100 * aliquota_720dias:.2f}")
elif tipoInvestimento == 1 and diasInvestidos > 720:
    print(F"O valor do imposto de renda a ser pago é R$: {valorResgatado / 100 * aliquotaMais720:.2f}")
elif tipoInvestimento == 2 or tipoInvestimento == 3:
    print(F"O valor do imposto de renda a ser pago é R$: 0.00")