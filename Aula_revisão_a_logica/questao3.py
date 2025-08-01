# 03 - Receba as notas dos 4 bimestres de um aluno, calcule a média e informe se ele esrá aprovado (média >= 6), em recuparação (média < 6) ou reprovado (média < 3)

bim1 = float(input('Digite a nota do primeiro bimestre: '))
bim2 = float(input('Digite a nota do segundo bimestre: '))
bim3 = float(input('Digite a nota do terceiro bimestre: '))
bim4 = float(input('Digite a nota do quarto bimestre: '))

media = (bim1 + bim2 + bim3 + bim4)/4

if media >= 6:
    print(f'Parabéns! Você foi aprovado. \n média: {media:.2f}')

elif media < 6 and media > 3:
    print(f'Infelizmente você ficou em recuperação... Mas não desista! \n média: {media:.2f}')

else:
    print(f'Você está reprovado... \n media: {media:.2f}')