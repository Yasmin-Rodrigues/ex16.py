#Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite seu nome completo:')).strip()
print('Todas as letras maiúsculas:',nome.upper())
print('Todas as letras minúsculas:',nome.lower())
print('Quantas letras ao todo:',len(nome))
print('A quantidade de caracteres do primero nome são:', len(nome.split()[0]))