# CONSTANTE = Variaveis que nao vao mudar
# Muitas condicoes no mesmo if(ruim)
#    <- contagem de complexidade(ruim)
 
velocidade = 67
local_carro = 89

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 

vel_carro_radar1 = velocidade > RADAR_1

carro_pass_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) 

carro_multado_radar1 = carro_pass_radar1 and vel_carro_radar1

if vel_carro_radar1:
    print("carro acima da velocidade permitida.")
else: 
    print("carro dentro da velocidade permitida.")

if carro_pass_radar1:
    print("carro passou radar 1.")

if carro_multado_radar1:
    print("Carro multado no radar")