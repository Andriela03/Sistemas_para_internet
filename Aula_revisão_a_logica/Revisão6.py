#Crie uma função que ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo, OBS: para formar um triângulo, o valor de cada lados deve ser menor que a soma dos outros 2 lados.

import math
def verifica_triangulo(A, B, C):
    if A < B + C and B < A + C and C < A + B:
        if A == B == C:
            l = A + B + C
            area = math.sqrt((3)* l**2)/4
            return f'O triângulo é equilátero. A área do triângulo é: {area}'
            
        elif A == B or B == C or A == C:
            if (A == B):
                base = C/2
                h = math.sqrt(base**2 + A**2)
                area = (C * h) / 2
                print(f'O valor da área é: {area}')  

            elif (A == C):
                base = C/2
                h = math.sqrt(base**2 + A**2)
                area = (C * h) / 2
                print(f'O valor da área é: {area}')  
            
            elif (C == B):
                base = C/2
                h = math.sqrt(base**2 + A**2)
                area = (C * h) / 2
                print(f'O valor da área é: {area}')  
        else:
            return 'O triângulo é escaleno.'
    else:
        return 'Essas medidas não formam um triângulo.'
    
# Isosceles = 2
# Equilátero = 3
# Escaleno = todos diferentes

print(verifica_triangulo(30, 20, 30))
 

 #Calcular a área do triangulo
    
