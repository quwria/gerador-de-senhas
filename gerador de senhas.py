import string
import random

def gerar_senha():
    abc = string.ascii_letters + string.digits
    simbs = ''.join(random.sample('!@#$%&', 2))
    senha = ''.join(random.choice(abc) for i in range(10)) + simbs
    senha = ''.join(random.sample(senha, len(senha)))
    return senha

print(gerar_senha())
