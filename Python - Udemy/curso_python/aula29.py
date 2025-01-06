"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
""" 
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_int = int(numero_str)
    print('INT:', numero_int)
    print(f'O dobro de {numero_str} é {numero_int * 2}')
except:
    print('Isso não é um número')