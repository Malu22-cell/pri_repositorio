# 1 - Par ou Ímpar
# Leia um número inteiro e informe se ele é par ou ímpar

num1 = 10
if num1 % 2 == 0:
    print("Numero PAR")
else:
    print("Numero IMPAR")

# 2 - Aprovado ou Reprovado 
# Leia a nota finaL de um aluno e diga se ele está:
# - Aprovado, se a nota for maior ou igual a 7. 
# - Reprovado, se a nota for menor que 7.

ap_1 = int(input("Digite a nota da ap_1"))
ap_2 = int(input("Digite a nota da ap_2"))
ac = int(input("Digite a nota da ac"))
media = 0.4*ap_1+0.4*ap_2*0.2*ac
if media >= 7:
    print("aprovado")
else:
    print("reprovado")

# 3 - Cálculo de Desconto
# - Leia o valor de uma compra.
# - Se o valor for maior que 100, aplicar 10% de desconto.
# - Caso contrário, não aplicar desconto.
# - Mostrar o valor final.

valor = float(input("Digite o valor da sua compra:"))
if valor > 100:
    desconto = valor*0.1
    preco_final = valor-desconto
    print(f"Compra totalizando:{preco_final}\n e desconto:{desconto}")
else:
    preco_final = valor
    print(f"Valor Final: {preco_final}")

# 4. Conversão de Temperatura
# Leia a temperatura em Celsius e converta para Fahrenheit usando a fórmula: F = (C x 9/5) + 32.

celsius = float(input("Digite a temperatura:"))
fahreinheit = (celsius*9/5) + 32
print(f"Temperatura em celsius {fahreinheit}")

# 5. Maior Número (Dois Valores)
# Leia dois números inteiros e informe:
# - Qual deles é o maior.
# - Ou se são iguais.

numero1 = int(input("Digite o numero1"))
numero2 = int(input("Digite o numero2"))
if numero1 > numero2:
    print("Primeiro é maior")
elif numero2 > numero1:
    print("Segundo é maior")
else:
    print("Os dois são iguais")

# 6. Maior Número (Três Valores)
# Escreva um programa que leia três números inteiros e determine qual deles é o maior.
# Entrada: Três números inteiros.
# Saída: O maior número.
# Exemplo:
# Entrada: 7, 2, 9
# Saída: 9

valor1 = int(input("Digite o valor1:"))
valor2 = int(input("Digite o valor2:"))
valor3 = int(input("Digite o valor3:"))

if valor1 > valor2 and valor2 > valor3:
    print(f"Print {valor1}")
elif valor1 > valor2 and valor2 > valor3:
    print(f"Print {valor2}")
elif valor1 > valor2 and valor2 > valor3:
    print(f"Print {valor3}")
else:
    print("Todas são iguais")

# 7 - . Calculadora Simples
# Crie uma calculadora simples que permita ao usuário realizar operações básicas: soma (+), subtração (-), multiplicação (*) e divisão (/).
# Entrada: Dois números e a operação desejada.
# Saída: O resultado da operação.
# Exemplo:
# Entrada: 8, 4, "/"
# Saída: 2

n1 = float(input("Digite o n1:"))
n2 = float(input("Digite o n2:"))
operacão = input("Digite a operacão:")
if operacão=="+":
    resultado=n1+n2
elif operacão=="-":
    resultado=n1-n2
elif operacão=="*":
    resultado=n1*n2
elif operacão=="/":
    if n2!=0:
        resultado=n1/n2
        print(f"Resultado é {resultado}")
    else:
        print("Divisão por zero")
else:
    print("Operacão invalida")


# 8 - Contagem de Números
# Leia uma sequência de números inteiros e conte quantos são positivos, negativos e zeros.
# Entrada: Lista de números inteiros (o usuário decide quantos números serão inseridos).
# Saída: Quantidade de números positivos, negativos e zeros.
# Exemplo:
# Entrada: [3, -1, 0, 7, -5]
# Saída: 2 positivos, 2 negativos, 1 zero

numeros = input("Digite uma sequência de números inteiros separados por espaço: ")
numeros = [int(x) for x in numeros.split()]

positivos = 0
negativos = 0
zeros = 0

for n in numeros:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        zeros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")

# 9 - Ano Bissexto
# Leia um número inteiro representando um ano e verifique se ele é bissexto ou não.
# Entrada: Um ano (número inteiro).
# Saída: "Bissexto" ou "Não é bissexto".
# Exemplo:
# Entrada: 2024
# Saída: Bissexto

ano = 2024
if ano % 4 == 0:
    print("Ano bissexto")
else:
    print("Ano nao bissexto")

# 10 - Intervalo de Idade
# Leia a idade de uma pessoa e informe se ela está na faixa etária permitida (18 a 65 anos).
# - Se a idade estiver entre 18 e 65 (inclusive), mostrar: "Dentro da faixa permitida".
# - Caso contrário, mostrar: "Fora da faixa permitida".
# (Use >= e <= com and).

idade = 19
if idade >= 18 and idade <= 65:
    print("Dentro da faixa permitida")
else:
    print("Fora da faixa permitida")

# 11 - Acesso ao Sistema
# Leia o usuário e a senha digitados.
# - Se usuário == "admin" e senha == "1234", mostrar: "Acesso permitido".
# - Caso contrário, mostrar: "Acesso negado".
# (Use == e and).

user = input("Digite o usuario:")
password = input("Digite a senha:")
if user=="eduardo" and password=="1357":
    print("Acesso permitido")
else:
    print("Acesso negado")

# 12 - Voto Obrigatório
# Leia a idade de uma pessoa.
# - Se a idade for menor que 16, mostrar "Não vota".
# - Se a idade for entre 18 e 70, mostrar "Voto obrigatório".
# - Caso contrário, mostrar "Voto facultativo".
# (Use combinações com and e or).

idade = int(input("Digite a idade:"))
if idade <= 16:
    print("Nao vota")
elif idade >= 18 and idade <= 70:
    print("voto obrigatorio")
else: 
    print("voto optativo")

# 13 - Número Fora de Intervalo
# Leia um número inteiro e verifique:
# - Se o número não está no intervalo de 10 a 50, mostrar "Fora do intervalo".
# - Caso contrário, mostrar "Dentro do intervalo".
# (Use not com >= e <=).

numero = int(input("Digite seu numero:"))
if not numero <= 10 and not numero >= 50:
    print("dentro do intervalo")
else:
    print("fora do intervalo")

# 14 - Aluno Aprovado com Recuperação
# Leia a média final de um aluno.
# - Se a média for >= 7, mostrar "Aprovado".
# - Se a média for >= 5 e < 7, mostrar "Recuperação".
# - Caso contrário, mostrar "Reprovado".
# (Use and, >=, <).

media_final = float(input("Digite a sua media:"))
if media_final >= 7:
    print("Aprovado")
elif media_final >= 5 and media_final < 7:
    print("recuperacao")
else:
    print("Reprovado")











