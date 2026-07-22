# Pegue os elementos de uma lista e faça uma nova lista, que não contenha nenhuma duplicata
# Faça com 2 funções: uma usando loop e criando a lista, e a outra usando set 
# Tentar intercalar as duas funções 

def constri():
    lista = [a[x] for x in range(len(a))]
    return limpa(lista)
    

def limpa(lista):
    lista_limpa = set(lista)
    return lista_limpa


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(constri())