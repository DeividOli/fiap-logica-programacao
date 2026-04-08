precoCarro = float(input("Digite o preço do carro: "))
desconto = precoCarro * 0.80

print(f"O preço final á vista com desconto 20% é: {desconto}")

for x in range(6, 66, 6):
    acrescimo = (x / 2 / 100) + 1
    precoFinal = precoCarro * acrescimo
    #print(f"O preço final parcelado em {x} é de R${precoCarro}, com pardelas de R${precoCarro / x}")
    print(f"O preço final parcelado em {x} é de R${precoFinal:.2f} com parcelas de R${precoFinal / x:.2f}")