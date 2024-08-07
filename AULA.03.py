NOTA1 = float(input("Digite a nota 1: "))
NOTA2 = float(input("Digite a nota 2: "))
NOTA3 = float(input("Digite a nota 3: "))

MEDIA = (NOTA1 + NOTA2 + NOTA3) / 3
print("A média do aluno é " + str(MEDIA))

if (MEDIA >= 7):
    print("Aluno APROVADO! Com média de: " + str(MEDIA))
    if(MEDIA > 5):
        print("Aluno está em RECUPERAÇÃO!")
else:
     print("Aluno está REPROVADO! Com média de: " + str(MEDIA))


#CRIAR AS VARIAVEIS: IDADE E TEM_CONVITE

idade = int(input("Digite sua idade:"))
tem_contite = True #booleano

if idade >= 18:
    if tem_contite:
        print("Pode entrar na festa!")
    else:
        print("Precisa de um covite paa entrar na festa.")
else:
    print("Não pode entrar. É menor de idade.")


