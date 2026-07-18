# Pegar a lista 'a' e mostrar os valores que são menores que 5 em outra lista
# mostrar a segunda lista em apenas uma linha   
# 
 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

for elementos in a:
    if elementos < 5:
        b.append(elementos)
print(b)


valor = int(input('Escreva um valor de corte da lista :\n'))
for elementos in a:
    if elementos < valor:
        c.append(elementos)
print(c)