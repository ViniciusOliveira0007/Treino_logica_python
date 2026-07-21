# Gerar duas listas randomicas, e fazer uma terceira tendo os valores iguais entre as listas    
# Usar lista compreeshion para fazer a terceira lista em uma linha

#[EXPRESSION FOR_LOOPS CONDITIONALS]

import random

lista_1 = range(random.randint(0,5), random.randint(5,10))
lista_2 = range(random.randint(0,5), random.randint(5,10))

#              |valor final|               loops       |  condição
lista_comum = set([ a for a in lista_1 for b in lista_2 if a == b ])
print(lista_1)
print(lista_2)

print(lista_comum)