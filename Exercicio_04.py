# Criar uma lista de números definida pelo usuário, definindo a entrada e saída com números
# A lista só pode aparecer com os divisores do número 


valor_inicial = int(input('Digite o primeiro valor da lista:\n'))
valor_final =  int(input('Digite o último valor da lista:\n'))

valor_final += 1
lista_usuario = range(valor_inicial, valor_final)


print('\n')
valor_dividido = int(input('Digite o valor que terá seus divisores mostrados:\n')) # valor que o usuário escolhe para ter seus divisores encontrados


lista_divisoria = []
for elementos in lista_usuario:
    if  valor_dividido % elementos == 0:
        lista_divisoria.append(elementos)

print(lista_divisoria)
