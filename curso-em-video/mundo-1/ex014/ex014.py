''' Exercício 014 - Escreva um programa que converta uma temperatura digitando em graus 
Celsius e converta para graus Farenheit. '''

celsius = float(input('Informe a temperatura em °C: '))
farenheit = (celsius * 1.8) + 32

print(f'A temperatura de {celsius}°C corresponde a {farenheit}°F!')