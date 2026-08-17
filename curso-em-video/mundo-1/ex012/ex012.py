''' Exercício 012 - Faça um algoritmo que leia o preçi de um produto e mostre o seu novo preço, 
com 5% de desconto. '''

preco = float(input('Qual é o preço do produto? R$ '))
novopreco = preco - (preco * 5/100)

print(f'O produto que custava R$ {preco:.2f} na promoção com desconto de 5% vai custar R$ {novopreco:.2f}.')