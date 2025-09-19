#Menores de 16 anos: Não pode votar 
#De 16 anos a 17 anos ou mais de 70: Voto opcional
#De 18 a 70 anos: O voto é obrigatório


idade = int(input("Digite sua idade: \n"))

if idade < 16:
    print("Você não pode votar")

elif idade == 16 or idade == 17 or idade > 70:
    print("Seu voto é opcional.")

else:
    print("Seu voto é obrigatório.")


# Peça para o usuário para o usuário digitar um número entre 1 e 10. Em Seguida, o programa deve exibir a tabuada desse número de 1 até 10.

numero = int(input("Digite um número: \n\n"))
for i in range(10):
    print(f"{numero} X {i} = {i * numero}")

#03 - Carlos está desenvolvendo um conversor de temperaturas. Crie um programa que receba
#uma temperatura em graus Celsius digitada pelo usuário e converta para Fahrenheit ou o
#contrário.

temp = float(input("Digite a temperatura em Celsius: \n"))

fahrenheit = (temp * 1.8) + 32
print(f"temperatura em fahrenheit = {fahrenheit}")


#04 - Crie um jogo onde o computador sorteia um número aleatório entre 1 e 20. O jogador
#tem 3 tentativas para adivinhar o número. Após cada tentativa, o programa deve dizer se o
#chute foi maior, menor ou igual ao número sorteado. Se o jogador acertar, o jogo termina
#com uma mensagem de parabéns. Se errar todas, o número correto é revelado.