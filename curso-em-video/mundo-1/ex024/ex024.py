''' Exercício 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não 
com o nome "SANTO". '''

cidade = str(input('Em qual cidade você nasceu? '))
prinome = cidade.split()
print(prinome[0].upper() == 'SANTO')