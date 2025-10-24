# 01 - Crie duas variáveis rem que A - 10 e B - 20, em seguida faça B = A de modo a obter os resultado finais A = 20 e B = 10.

# A = 10
# B = 20 
# C = B 

# A = B
# B = A


# usuario_1 = "José"
# usuario_2 = "Maria"

# print("Usuário 1:", usuario_1)
# print("Usuário 1:", usuario_2)

# troca_usuario = usuario_1
# usuario_1 = usuario_2
# usuario_2 = troca_usuario

# print("Usuário 1:", usuario_1)
# print("Usuário 2:", usuario_2)


#02 - Crie uma função que recebe um valor e retorna a informação dizendo se é um valor positivo, negativo ou nulo.
# def Valor(valor):
#     if valor > 0:
#         return 'O número é positivo.'

#     elif valor < 0:
#         return 'O número é negativo.'
    
#     elif valor == 0 :
#         return 'O valor é nulo'

#     else:
#         return 'Valor inválido.'

# print(Valor(30))

# 03 - O custo de um carro novo ao consumidor é a soma do de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

def calcular_custo(custo_fabrica):
    imposto_distribuidor = custo_fabrica * (28/100)
    imposto_geral = custo_fabrica * (45/100)
    custo_total = custo_fabrica + imposto_distribuidor + imposto_geral
    return custo_total

print(calcular_custo(1000))
