from random import randint
from time import sleep

print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 30)
computador = randint(0,5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1.5)

if computador == num:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {num}!')