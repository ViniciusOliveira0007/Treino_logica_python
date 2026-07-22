# Fazer o usuário escrever uma frase contendo muitas palavras, e retornar para ele em outra ordem 
# Usar funções

def subString(frase):
    frase_cortada = frase.split()
    print(f'{frase_cortada[-1]}, {' '.join(frase_cortada[:-1])}')

    pass

frase = input('Se apresente:\n')

subString(frase)