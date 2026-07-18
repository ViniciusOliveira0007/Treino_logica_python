#Fazer o usuário escrever o nome e a idade dele, para mostrar qual será o ano que ele fará 100 anos

nome = input('Escreva o seu nome:\n')
idade = int(input('Escreva a sua idade:\n'))

tempo_restante = 100 - idade
ano_seculo = 2026 + tempo_restante

mensagem = f'O ano que você irá fazer 100 anos de idade é: {ano_seculo}'

print(mensagem)

vezes = int(input('Escreva uma quantidade de vezes para se repetir:\n'))

print(vezes * f'{mensagem}\n')
