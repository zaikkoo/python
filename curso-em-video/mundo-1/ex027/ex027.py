''' Exercício 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em 
seguida o primeiro e o último separadamente. 

Ex: Ana Maria de Souza (primeiro = Ana; último = Souza).'''

nome = str(input('Digite o seu nome completo: ').strip())
separado = nome.split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {separado[0]}')
print(f'Seu último nome é {separado[-1]}')