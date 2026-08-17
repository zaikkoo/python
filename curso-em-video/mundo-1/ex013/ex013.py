''' Exercício 013 - Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, 
com 15% de aumento. '''

salario = float(input('Qual é o salário do funcionário? R$ '))
novosalario = salario + (salario * 15/100)

print(f'Um funcionário ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber R$ {novosalario:.2f}.')