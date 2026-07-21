# Pedir um número para o usuário e dizer se o número é um número primo ou não
# Utilizar de funções para isso


def verifica_primo(lista_usuario, valor_dividido):
    lista_divisoria = []
    for elementos in lista_usuario:
        if  valor_dividido % elementos == 0:
           lista_divisoria.append(elementos)

    if len(lista_divisoria) == 2:
        if lista_divisoria[0] == 1:
            if lista_divisoria[1] == valor_dividido:
               return 'O número é primo'
            else:
                return 'Não é primo' 
        else:
            return 'Não é primo'
    else:
        return 'Não é primo'


valor_dividido = int(input('Digite o valor que terá seus divisores mostrados:\n')) # valor que o usuário escolhe para ter seus divisores encontrados
valor_final = valor_dividido + 1
lista_usuario = range(1, valor_final)

print(verifica_primo(lista_usuario, valor_dividido))

