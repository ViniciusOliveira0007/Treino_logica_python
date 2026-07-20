# Gerar um número aleatório entre 1 e 9, incluindo 1 e 9
# O usuário deve ir testando até acertar, a menos que ele escreva exit, ele continuará no jogo
# Depois de ele sair, deve mostrar a quantidade de vezes que ele tentou

import random


a = random.randint(1,9)
contador = 0
ficar = True
while ficar == True:
    contador += 1
    resposta = 0

    resposta = int(input('Chute um valor de 1 a 9\n'))
    if resposta == a:
        print('Você acertou!!!')
        verifica = input('Deseja sair ?\n')
        if verifica == 'sim':
            ficar = False

    elif resposta < a:
        print('Você chutou baixo\n')
        verifica = input('Deseja sair ?\n')
        if verifica == 'sim':
            ficar = False
    else:
        print('Você chutou alto\n')
        verifica = input('Deseja sair ?\n')
        if verifica == 'sim':
            ficar = False

    

print(f'Você tentou {contador} de vezes\n')
