distancia = float(input('Digite a distância da sua viagem: '))

print(f'Você está prestes a começar uma viagem de {distancia}km.')

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'E o preço da sua passagem será de R$ {preco:.2f}.')