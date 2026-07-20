# Pegar os elementos da lista 'a', e fazer uma nova lista, como apenas os elementos pares dela.
# tentar fazer isso em apenas uma linha


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print( [i for i in a if i % 2 == 0 ])


''' 
lista_pares = []

for i in a:
    if i % 2 == 0:
        lista_pares.append(i)
print(lista_pares)


'''