import math

angulo = float(input('Digite o ângulo que você deseja: '))
radianos = math.radians(angulo)
sen = math.sin(radianos)
cos = math.cos(radianos)
tan = math.tan(radianos)

print(f'O ângulo de {angulo} tem o SENO de {sen:.2f}.')
print(f'O ângulo de {angulo} tem o COSSENO de {cos:.2f}.')
print(f'O ângulo de {angulo} tem o TANGENTE de {tan:.2f}.')