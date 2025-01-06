while True:
    num1 = input("Digite um numero: ")
    num2 = input("Digite outro numero: ")
    operador = input("Digite o operador: (+-*/)")
    num_valido = None

    try:
        num1_float = int(num1)
        num2_float = int(num2)
        num_valido = True
    
    except:
        num_valido = None
    
    operador_permitido = "+-*/"  
    
    if operador not in operador_permitido:
        print("Digite um operador válido")
        continue   
    
    elif len(operador) > 1:
        print("Digite apenas um operador")
        continue
    
    elif num_valido is None:
        print("Um ou mais numeros digitados são inválidos.")
        continue
    
    elif operador == "+":
        result_adicao = num1_float + num2_float
        print(result_adicao)
        
    elif operador == "-":
        result_subtracao = num1_float - num2_float
        print(result_subtracao)
    
    elif operador == "*":
        result_multiplicacao = num1_float * num2_float
        print(result_multiplicacao)
                    
    if operador == "/":
        result_divisao = num1_float / num2_float
        print(result_divisao)
        
    elif num2_float == 0:
        print("Não é possível dividir por zero")
        
    sair =  input("Deseja sair? [S]im: ").lower().startswith('s')
    
    if sair == True:
        break