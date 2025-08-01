#01 - Utilizando if/else simular a operação de uma calculadora. Que deverá receber dois números e um operador. Se o número for + (somar), * (multiplicar) e / (dividir)
import time

numero1 = float(input('Escolha um número: '))
numero2 = float(input('Escolha outro numero: '))

escolha = str(input('Qual operação você deseja fazer? \n a) Somar \n b) Subtrair \n c) Multiplicar \n d) Dividir \n \n  '))


if escolha == 'a':
    soma = numero1 + numero2
    print('Somando os dois números...')
    time.sleep(2)
    print(soma)

elif escolha == 'b':
    subtrair = numero1 - numero2
    print('Subtraindo os dois números...')
    time.sleep(2)
    print(subtrair)

elif escolha == 'c':
    multiplicar = numero1 * numero2
    print('Multiplicando os dois números...')
    time.sleep(2)
    print(multiplicar)

elif escolha == 'd':
    if numero2 == 0:
        print('Não é possível dividir por zero')

    else:
        dividir = numero1 / numero2
        print('Dividindo os dois números...')
        time.sleep(2)
        print(f"{dividir:.2f}")

else:
    print('Opção inválida.')
