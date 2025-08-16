nome = str(input('Digite o seu nome completo: '))
print('Analisando seu nome...')

print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome. lower()}.')
print(f'Seu nome tem ao todo tem {len(nome) - nome.count(' ')} letras.')
prinome = nome.split()
print(f'Seu primeiro nome é {prinome[0]} e ele tem {len(prinome[0])} letras.')