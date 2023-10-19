"""AULA 02 - DIA 17/08/2023"""

# EXERCÍCIO 03
ESTADO_DA_MEMÓRIA = 0
def calculadora(a):
    global ESTADO_DA_MEMÓRI
    print("Opções:"
          "(1) Somar",
          "(2) Subtrair",
          "(3) Multiplicar",
          "(4) Dividir)",
          "(5) Limpar a Memória",
          "(6) Sair do Programa")

    opção = int(input("Selecione a opção: "))
    if opção == 1:
        soma = ESTADO_DA_MEMÓRIA + int(input("Digite um número: "))
        return print(soma)
    elif opção == 2:
        subtração = (ESTADO_DA_MEMÓRIA) - int(input("Digite um número: "))
        return print(subtração)
    elif opção == 3:
        multiplicação = (ESTADO_DA_MEMÓRIA) * int(input("Digite um número: "))
        return print(multiplicação)
    elif opção == 4:
        divisão = (ESTADO_DA_MEMÓRIA) / int(input("Digite um número: "))
        return print(divisão)
    elif opção == 5:
        ESTADO_DA_MEMÓRIA = 0
        return print(ESTADO_DA_MEMÓRIA)
    elif opção == 6:
        print("Fechando o Programa.")