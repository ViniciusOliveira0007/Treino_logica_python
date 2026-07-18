#Verificar se um número é par ou impar
#e depois verificar se pode ser dividido por 4, e se sim, efetuar outra operação com isso

numero = int(input('Escreva um número:\n'))
verifica = numero % 2
if verifica == 0:
    print('O número é par\n')
else:
    print('O número é ímpar\n')


verifica_02 = numero % 4
if verifica_02 == 0:
    num = int(input('Digite um número ao qual vai ser dividido:\n'))
    check = int(input('Digite um número ao qual irá dividir:\n'))
    verifica_03 = num % check

    if verifica_03 == 0:
        print('O numero pode ser dividido.\n')
    else:
        print('O número não pode ser dividido.\n')
else:
    print('O numero não é divisivel por 4\n')