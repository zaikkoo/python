''' Exercício 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto 
adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. '''

import math

catoposto = float(input('Comprimento do cateto oposto: '))
catadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catoposto, catadjacente)

print(f'A hipotenusa vai medir {hipotenusa:.2f}.')