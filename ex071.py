'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
from time import sleep
print('-----' * 8)
print('{:^40}'.format('Banco FeltDEV'))
print('-----' * 8)
valor = int(input('Quanto você deseja sacar? R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Aqui estão {totalced} de {ced}')
        if ced == 50:
            ced = 20 #não precisa escrever o código que foi escrito lá em cima..
        elif ced == 20:#aqui é um else, que volta a fazer os testes dentro do while mudando o valor da variável.
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
        totalced = 0
print('Confira seu saque!!')
print('-----' * 8)
print('Obrigado por usar nossos serviços.\nO Banco FeltDEV agradece. Volte sempre!!')