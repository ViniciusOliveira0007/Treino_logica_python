# fazer dois jogadores jogarem pedra papel e tesoura
# depois de terminado, perguntar se eles querem jogar um novo jogo

condicao = True
while condicao == True:
    jogada_1 = input('Faça sua jogada, jogador 1:\n')
    jogada_2 = input('Faça sua jogada, jogador 2:\n')

    if jogada_1 == 'Pedra' and jogada_2 == 'Tesoura':
        print('Jogador 1 venceu\nPARABÉNS')
        new_game = input('Desejam jogar novamente ?\nYes\t||\tNo\n\n')
        if new_game == 'Yes':
            condicao = True
        else:
            condicao = False

    elif jogada_1 == 'Tesoura' and jogada_2 == 'Papel':
        print('Jogador 1 venceu\nPARABÉNS')
        new_game = input('Desejam jogar novamente ?\nYes\t||\tNo\n\n')
        if new_game == 'Yes':
            condicao = True
        else:
            condicao = False

    elif jogada_1 == 'Papel' and jogada_2 == 'Pedra':
        print('Jogador 1 venceu\nPARABÉNS')
    
        new_game = input('Desejam jogar novamente ?\nYes\t||\tNo\n\n')
        if new_game == 'Yes':
            condicao = True
        else:
            condicao = False

    elif jogada_1 == jogada_2:
        print('Isso é um EMPATE')
        new_game = input('Desejam jogar novamente ?\nYes\t||\tNo\n\n')
        if new_game == 'Yes':
            condicao = True
        else:
            condicao = False

    else:
        print('Jogador 2 venceu\nPARABÉNS')       
       
        new_game = input('Desejam jogar novamente ?\nYes\t||\tNo\n\n')
        if new_game == 'Yes':
            condicao = True
        else:
            condicao = False


print('Você saiu do jogo')