nome = str(input('Digite o seu nome completo: ').strip())
separado = nome.split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {separado[0]}')
print(f'Seu último nome é {separado[-1]}')