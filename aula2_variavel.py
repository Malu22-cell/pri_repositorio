# identificação de Tipos:
# 1 - Crie variáveis que representem:
# sua idade 
idade = 46
# sua altura
altura = 1.69
# seu nome
nome = "Malu"
# se você é estudante
eh_estudante = True
# para ver o tipo de variavel
type(eh_estudante)

# 2 - O usuario digita a sua idade 
# -  Converta essa entrada para o numero inteiro
# -  Some +5 anos e mostre o resultado.
idade = input("Digite a sua idade:")
idade = int(idade)
type(idade)
idade = int(idade) + 5
print(idade)

# 3 - Soma de numeros inteiros 

numero_1 = input("Digite 1 numero:")
numero_2 = input("Digite outro numero")

numero_1 = int(numero_1)
numero_2 = int(numero_2)

soma = (numero_1 + numero_2)
print(soma)

# 4 - Média de Três Números Inteiros Enunciado

numero_3 = input("Digite 1 numero")
numero_4 = input("Digite outro numero")
numero_5 = input("Digite mais um numero")

numero_3 = int(numero_3)
numero_4 = int(numero_4)
numero_5 = int(numero_5)

media = (numero_3 + numero_4 + numero_5)/3
print(media)

# 5 - Media Ponderada (Padrao IBMEC)

ap1 = float(input("Digite sua nota da Ap1"))
ap2 = float(input("Digite outro nota da Ap2"))
ac = float(input("Digite mais um numero da AC"))

media_notas = (ap1*0.4+ap2*0.4+ac*0.2)
print(media_notas)

# 6 - Manipulacao de Strings

nome_usuario = input("Digite seu nome completo?:")

nome_usuario.upper()

primeiro_nome = nome_usuario.split()[0]

len_nome_usuario = len(primeiro_nome)

print(len_nome_usuario)
