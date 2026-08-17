''' Exercício 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é 
PAR ou ÍMPAR. '''

num = int(input('Me diga um número qualquer: '))

if num % 2 == 0:
    print(f'O número {num} é Par.')
else:
    print(f'O número {num} é ímpar.')