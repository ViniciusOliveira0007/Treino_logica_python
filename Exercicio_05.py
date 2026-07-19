# OBJETIVO: encontrar elementos em comum entre as listas, e mostralas 
# fazer as listas randomicas em uma linha

a = range(2, 15)
b = range(3, 52)

comum = []

for elementos in a:    
    if elementos in b:
        comum.append(elementos)

print(comum)


'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(set(a[x] for x in range(len(a))if a[x] in b))

'''