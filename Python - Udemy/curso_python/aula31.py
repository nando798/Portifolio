"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = False
passou_no_if = True


if condicao:
    passou_no_if = True
    print("faça algo")
else: 
    print("Não faça algo")
    
print(passou_no_if, passou_no_if is None)

if passou_no_if is None:
    print("Passou no if") 
    
if passou_no_if is not None:
    print("Não passou no if")
    
