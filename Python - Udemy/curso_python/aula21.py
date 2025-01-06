# Operadores lógicos
# And, or, not
#and - todas as condicoes precisam ser verdadeiras
# se qualqeur valor for considerado falso, 
# a expressao inteira derá avalioada como falso,
# a expressao inteira será avaliada naquele valor
# são considerados falsy ( que você ja viu)
# 0 0.0 '' False
# também existe o tipo None que é 
#usado para representar um não valor

entrada = input("[E]ntrar [S]air ")
senha_digitada = input("Digite a senha: ")
senha_permitida = "117997"

if entrada == 'E' and senha_digitada == senha_permitida:
    print("entrar")
else:
    print("sair")    

