# Operadores lógicos
# And, or, not
#or - todas as condicoes precisam ser verdadeiras
# se qualquer valor for considerado verdadeiro, 
# a expressao inteira derá avaliada como verdadeira,
# a expressao inteira será avaliada naquele valor
# são considerados falsy ( que você ja viu)
# 0 0.0 '' False
# também existe o tipo None que é 
#usado para representar um não valor

entrada = input("[E]ntrar [S]air ")
senha_digitada = input("Digite a senha: ")
senha_permitida = "`123456`"

if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
    print("entrar")
else:
    print("sair")    

