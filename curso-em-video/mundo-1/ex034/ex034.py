salario = float(input('Qual é o salário do funcionário? R$ '))

if salario <= 1250:
    novosal = salario + (salario * 15/100)
else:
    novosal = salario + (salario * 10/100)

print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {novosal:.2f} agora.')