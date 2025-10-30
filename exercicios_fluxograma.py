# 1. Escolher Roupa para Sair
# Enunciado:
# Crie um algoritmo descritivo para escolher a roupa de acordo com o clima:
# - Se estiver frio (temperatura abaixo de 20°C), vestir casaco.
# - Caso contrário, vestir camiseta.
# - Ao final, colocar calça e sapatos.

temperatura = float(input("Digite a temperatura em C:"))
if temperatura < 20:
    print("Vestir casaco")
else:
    print("Vestir camiseta")

print("Colocar calça e sapato")

# 2. Decidir Transporte para o Trabalho
# Enunciado:
# Escreva um algoritmo que, ao acordar, decide qual transporte usar:
# - Se o carro estiver com combustível suficiente, ir de carro.
# - Caso contrário, verificar se há dinheiro para transporte público:
# - Se sim, ir de ônibus.
# - Se não, ir a pé.

combustivel = input("O carro tem combustivel suficiente? (sim/não):").lower()
if combustivel == "sim":
    print("Ir de carro")
else:
    dinheiro = input("Você tem dinheiro para tranporte público? (sim/não):").lower()
    if dinheiro == "sim":
        print("Ir de onibus")
    else:
        print("Ir a pé")


# 3. Verificar Saldo antes de Comprar
# Você está em uma loja e quer comprar um produto:
# - Ler o valor do produto e o saldo disponível.
# - Se o saldo for maior ou igual ao valor do produto, comprar.
# - Caso contrário, exibir mensagem de saldo insuficiente.



# 4. Preparar Lanche
# Você quer fazer um sanduíche:
# - Se tiver pão, continuar. Caso contrário, encerrar o algoritmo com a mensagem “Sem pão, não é possível fazer o lanche”.
# - Se tiver queijo, adicionar. Caso contrário, usar presunto.
# - Se tiver tomate, adicionar.
# - Servir o sanduíche.


# 5. Contagem de 1 até 10
# Desenhe um fluxograma que mostre os números de 1 até 10, um por vez.


# 6. Tabuada
# Desenhe um fluxograma que leia um número inteiro n e mostre a tabuada desse número, do 1 até o 10.


# 7. Leitura de Temperaturas Diárias (com repetição)
# Crie um algoritmo que:
# - Leia a temperatura de 7 dias da semana.
# - Para cada temperatura:
# - Se for maior que 30°C, exibir “Dia quente”.
# - Caso contrário, exibir “Dia agradável”.
# Ao final, encerrar o algoritmo.

lista_temperatura = [10,20,30,40,50,60,70]
for temp in lista_temperatura:
    if temp > 30:
        print("Dia quente")
    elif temp <= 10:
        print("Dia frio")
    else:
        print("Dia agradável")



# 8. Senha correta 
# Desenhe um fluxograma que: 
# •	Peça uma senha ao usuário.
# •	Enquanto a senha digitada for diferente de 1234, peça novamente.
# •	Quando a senha for correta, mostre a mensagem “Acesso permitido”.


# 9. Contagem regressiva
# Desenhe um fluxograma que:
# •	Leia um número inteiro n.
# •	Mostre os números de n até 0, em ordem decrescente.
# •	Ao final, mostre a palavra “Fim”.

n = int(input("Digite um numero inteiro"))
while n >= 0:
    print(n)
    n = n-1 
    print("Fim")


# 10. Soma até número negativo
# Desenhe um fluxograma que:
# •	Leia vários números inteiros.
# •	Some todos os números digitados.
# •	O processo deve parar quando o usuário digitar um número negativo.
# •	Ao final, mostre a soma total.
