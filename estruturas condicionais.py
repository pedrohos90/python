MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda nao pode tirar a CNH")

# acima esta o primeiro exemplo de estrutura condicional, usando o IF maior ou igual e IF menor
# abaixo o segundo exemplo, usando IF e ELSE



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("ainda nao pode tirar a CNH")


# agora o exemplo do ELIF

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas nao pode fazer aulas praticas.")
else:
    print("ainda nao pode tirar a CNH")    