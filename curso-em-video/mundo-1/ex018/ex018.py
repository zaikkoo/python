''' Exercício 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do 
seno, cosseno e tangente desse ângulo. '''

import math

angulo = float(input('Digite o ângulo que você deseja: '))
radianos = math.radians(angulo)
sen = math.sin(radianos)
cos = math.cos(radianos)
tan = math.tan(radianos)

print(f'O ângulo de {angulo} tem o SENO de {sen:.2f}.')
print(f'O ângulo de {angulo} tem o COSSENO de {cos:.2f}.')
print(f'O ângulo de {angulo} tem o TANGENTE de {tan:.2f}.')