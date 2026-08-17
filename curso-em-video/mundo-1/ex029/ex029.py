''' Exercício 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 
80 Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada 
Km acima do limite. '''

velocidade = float(input('Qual é velocidade atual do carro? '))

if velocidade > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80 km/h.')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R$ {multa:.2f}!')

print('Tenha um bom dia! Dirija com segurança!')