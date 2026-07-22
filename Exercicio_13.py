# Fazer o usuário entrar com um número que a quantidade de números na sequência de Fibonnaci
# Usar Funções 
# A sequência de Fibonnaci é que o próximo número é a soma dos dois números anteriores


def Fibonnaci(quantidade):
    
    lista = [1,1,2,3]
    if quantidade > 4:
        while len(lista) < quantidade :
            lista.append(lista[-1] + lista[-2])
        #lista_fibo = [i for i in lista if i < quantidade]
        print(lista)
    else:
        lista_fibo = lista[:quantidade]
        print(lista_fibo)


quantidade = int(input('Digite a quantidade da lista de Fibonnaci que deseja?\n'))
Fibonnaci(quantidade)