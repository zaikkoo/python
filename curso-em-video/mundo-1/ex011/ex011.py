largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')