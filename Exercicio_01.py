colaboradores = int(input("Digite a quantidade de colaboradores: "))
contagem = [0, 0, 0, 0, 0]
diasSemanas = ["segunda-feira", "terca-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
numeroRes = 0

while numeroRes < colaboradores:
    resposta = input(f"Digite a sua preferencia (Segunda-feira, Terca-feira, Quarta-feira, Quinta-feira, Sexta-feira)").lower()
    if resposta in diasSemanas:
        numeroRes += 1
    else:
        print("Escolha um dia válido!")
        
    if resposta == diasSemanas[0]:
        contagem[0] += 1
    elif resposta == diasSemanas[1]:
        contagem[1] += 1
    elif resposta == diasSemanas[2]:
        contagem[2] += 1
    elif resposta == diasSemanas[3]:
        contagem[3] +=1
    elif resposta == diasSemanas[4]:
        contagem[4] += 1

maiorValor = max(contagem)
qtdNumLista = contagem.count(maiorValor)
indice = contagem.index(maiorValor)
if  qtdNumLista >= 2:
    print("Deu empate!")
else:
    print(f"O dia escolhido pelos colaboradores foi: {diasSemanas[indice]}")
