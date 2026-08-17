''' Exercício 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos 
dígitos separados.'''

num = int(input('Digite um número: '))
print(f'Analisando o número {num}.')

uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10

print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {mil}')