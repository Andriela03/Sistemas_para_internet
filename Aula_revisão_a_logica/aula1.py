#01 - Se o usuário tiver +18 (imprimir mensagem)
#     se menor que 18 (imprimir mensagem)


#idade = int(input('Qual é a sua idade? '))

#if idade >= 18:
    #print('Você pode acessar esse conteúdo.')

#elif idade < 0:
    #print('mensagem inválida.') 

#elif idade <=

#else: 
    #print('Você não pode acessar esse conteúdo.')


#02 - Se o usuário tiver + 18 (imprimir mensagem)
#     se menor de 18 anos (imprimir mensagem)
#     menor de 18 e maior de 16, estiver acompanhado ele poderá entrar (imprimir mensagem)
#     se a idade negativa (imprimir mensagem)


idade = int(input('Qual é a sua idade? '))

if idade >= 18:
    print('Você pode acessar esse conteúdo.')

elif idade < 0:
    print('mensagem inválida.') 

elif idade >= 16 and idade < 18:
    acompanhado = str(input('Você está acompanhado?'))

    if acompanhado == "sim":
        adulto = int(input('Qual é a idade da pessoa que está com você?'))
        if adulto >= 18:
            print('Você pode acessar esse conteúdo.')
        else:
            print('Você pode acessar esse conteúdo.')     

    elif acompanhado == 'não':
        print('você não pode acessar.')
    else:
        print('Mensagem inválida.')
else: 
    print('Você não pode acessar esse conteúdo.')