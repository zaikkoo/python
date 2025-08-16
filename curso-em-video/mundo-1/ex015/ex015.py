dias = int(input('Quantos dias alugados? '))
distancia = int(input('Quantos Km rodados? '))
preco = (dias * 60) + (distancia * 0.15)

print(f'O total a pagar é de R$ {preco:.2f}.')