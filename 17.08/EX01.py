# AULA 02 - DIA 17/08/2023

"""ALTERAÇÃO DE LISTA"""

def zera(x):
    for i in range(len(x)):
        x[i] = 0

a = [1, 2, 3]
zera(a)
print(a)
