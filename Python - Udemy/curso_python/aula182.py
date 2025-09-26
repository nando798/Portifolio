# secrets gera dados criptograficamente seguros

import secrets
import string as s
from secrets import SystemRandom as sr

# print("".join(sr().choices(s.ascii_lowercase + s.digits, k=8)))

random = secrets.SystemRandom()

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(20) Nao faz nada!!!
# random.randrange(início, fim, passo)
r_range = random.randrange(10, 20)
print(r_range)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
# random.randint(início, fim)
r_int = random.randint(10, 20)
print(r_int)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
# random.uniform(início, fim)
r_uniform = random.uniform(10, 20)
print(r_uniform)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ["Luiz", "Maria", "Helena", "João"]
random.shuffle(nomes)
print(nomes)
# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=2)
print(nomes)
print(novos_nomes)
# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)
# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))
