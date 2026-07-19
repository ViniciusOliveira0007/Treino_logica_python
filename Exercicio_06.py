# Fazer um string ser uma lista, e verificar se a palavra é a mesma coisa de trás para frente
# 
# 

a = [3, 4, 5, 6, 7, 8, 9]
a.reverse()
print(a)


palavra = input('Digite uma palavra:\n')

lista = []
for i in palavra:
    lista.append(i)

print(lista)
lista_reversa = lista[::-1]

print(lista_reversa)

if lista == lista_reversa:
    print('A palavra é um palindrome')

else:
    print('não é um palindrome')