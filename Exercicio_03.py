valorDivida = float(input("Digite o valor da divida: "))
controleJuros = 1.10
numParcelas = 3
print(f"Total: R$ {valorDivida} Juros:R$ {0:.2f} Numero de parcelas:{1} Valor da parcela:R$ {valorDivida:.2f}")
for i in range(1, 5):
    valorAcrescimo = valorDivida * controleJuros
    print(f"Total:R$ {valorDivida * controleJuros:.2f} Juros: R${valorAcrescimo - valorDivida:.2f} Numero de parcelas: {numParcelas} Valor da parcela:R$ {valorAcrescimo / numParcelas:.2f}")
    controleJuros += 0.05
    numParcelas += 3