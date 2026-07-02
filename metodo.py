import random

# 1 

def atividade1():
    return random.randint(5, 10)

# 2 

def atividade2():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    return x, y, z

# 3 

def atividade3():
    numeros = list(range(10, 31))
    return random.choice(numeros)

# 4
 
def atividade4():
    for i in range(10, 0, -1):
        print(i)
    print("Fogo!")

# 5 

def atividade5(numero):
    soma = 0

    if numero > 0:
        for i in range(2, numero + 1, 2):
            soma += i
        return soma
    else:
        return "Digite um número positivo."

# 6 

def atividade6(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7 

def atividade7():
    for i in range(99, 0, -2):
        print(i)