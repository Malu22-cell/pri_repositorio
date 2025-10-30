# Exercício 1 – Faturamento diário
# Você tem um registro de vendas de uma loja durante a semana:
# faturamento = [
 #{"dia": "segunda", "valor": 1200},
 #{"dia": "terça", "valor": 1500},
 #{"dia": "quarta", "valor": 900},
 #{"dia": "quinta", "valor": 1800},
 #{"dia": "sexta", "valor": 2400},]

faturamento = [{"dia": "segunda", "valor": 1200},
    {"dia": "terça",   "valor": 1500},
    {"dia": "quarta",  "valor": 900},
    {"dia": "quinta",  "valor": 1800},
    {"dia": "sexta",   "valor": 2400},
]

# Faturamento total da semana
total = sum(d["valor"] for d in faturamento)

# Dia de maior faturamento
maior_dia = max(faturamento, key=lambda d: d["valor"])  # retorna o dict com maior "valor"

# Média de vendas
media = total / len(faturamento)

print(f"Faturamento total: R$ {total:.2f}")
print(f"Maior faturamento: {maior_dia['dia']} (R$ {maior_dia['valor']:.2f})")
print(f"Média de vendas: R$ {media:.2f}")


# Exercício 2 – Estoque de produtos
# Uma empresa tem o seguinte estoque:
# estoque = { # estoques em 3 filiais
# "notebook": [5, 7, 3],  
# "mouse": [20, 25, 18],
# "teclado": [12, 14, 9],}

estoque = {
    "notebook": [5, 7, 3],
    "mouse": [20, 25, 18],
    "teclado": [12, 14, 9]
}

# Calcule o estoque total de cada produto
totais = {}
for produto, quantidades in estoque.items():
    totais[produto] = sum(quantidades)

# Descubra qual produto tem o menor estoque total
menor_produto = min(totais, key=totais.get)

# Transforme os totais em um novo dicionário
novo_estoque = totais.copy()

print("Totais por produto:", totais)
print(f"Produto com menor estoque total: {menor_produto} ({totais[menor_produto]} unidades)")
print("Novo dicionário de estoque:", novo_estoque)


# Exercício 3 – Funcionários e salários
# Considere a lista de funcionários:
# funcionarios = [
# {"nome": "Ana", "salario": 4500, "departamento": "RH"},
# {"nome": "Carlos", "salario": 7000, "departamento": "TI"},
# {"nome": "Beatriz", "salario": 5200, "departamento": "Financeiro"},
# {"nome": "João", "salario": 4800, "departamento": "TI"},]

funcionarios = [
    {"nome": "Ana", "salario": 4500, "departamento": "RH"},
    {"nome": "Carlos", "salario": 7000, "departamento": "TI"},
    {"nome": "Beatriz", "salario": 5200, "departamento": "Financeiro"},
    {"nome": "João", "salario": 4800, "departamento": "TI"},
]

# Calcule a folha salarial total da empresa
folha_total = sum(f["salario"] for f in funcionarios)

# Descubra qual funcionário ganha mais
maior_salario = max(funcionarios, key=lambda f: f["salario"])

# Agrupe os salários por departamento
salarios_por_departamento = {}
for f in funcionarios:
    dep = f["departamento"]
    if dep not in salarios_por_departamento:
        salarios_por_departamento[dep] = []
    salarios_por_departamento[dep].append(f["salario"])


print(f"Folha salarial total: R$ {folha_total:.2f}")
print(f"Funcionário com maior salário: {maior_salario['nome']} (R$ {maior_salario['salario']:.2f})")
print("Salários por departamento:")
for dep, salarios in salarios_por_departamento.items():
    print(f"  {dep}: {salarios}")


# Exercício 4 – Pesquisa de satisfação
# Uma pesquisa coletou avaliações de clientes (0 a 10):
# avaliacoes = {
# "loja A": [8, 9, 7, 10, 6],
# "loja B": [5, 7, 6, 8, 7],
# "loja C": [9, 8, 9, 10, 9],}

avaliacoes = {
    "loja A": [8, 9, 7, 10, 6],
    "loja B": [5, 7, 6, 8, 7],
    "loja C": [9, 8, 9, 10, 9]
}

# Calcule a média de satisfação de cada loja
medias = {}
for loja, notas in avaliacoes.items():
    medias[loja] = sum(notas) / len(notas)

# Descubra qual loja tem a maior média
melhor_loja = max(medias, key=medias.get)

# Gere um dicionário só com as médias
medias_lojas = medias.copy()

# Exibição dos resultados
print("Médias de satisfação por loja:")
for loja, media in medias_lojas.items():
    print(f"{loja}: {media:.2f}")

print(f"\nA loja com a maior média é: {melhor_loja} ({medias[melhor_loja]:.2f})")


#Exercício 5 – Controle de vendas
#Os vendedores registraram suas vendas do mês:
#vendas = [
# {"vendedor": "Marcos", "itens": {"notebook": 2, "mouse": 5}},
# {"vendedor": "Lucia", "itens": {"notebook": 1, "teclado": 3}},
# {"vendedor": "Paula", "itens": {"mouse": 4, "teclado": 2}},]

vendas = [
    {"vendedor": "Marcos", "itens": {"notebook": 2, "mouse": 5}},
    {"vendedor": "Lúcia",  "itens": {"notebook": 1, "teclado": 3}},
    {"vendedor": "Paula",  "itens": {"mouse": 4, "teclado": 2}},
]

# Calcule quantos notebooks foram vendidos no total
total_notebooks = sum(v["itens"].get("notebook", 0) for v in vendas)

# Descubra qual vendedor vendeu mais itens no mês
maior_vendedor = max(vendas, key=lambda v: sum(v["itens"].values()))
total_itens_vendedor = sum(maior_vendedor["itens"].values())

# Monte um dicionário consolidando o total de cada produto
totais_produtos = {}
for v in vendas:
    for produto, quantidade in v["itens"].items():
        if produto not in totais_produtos:
            totais_produtos[produto] = 0
        totais_produtos[produto] += quantidade

print(f"Total de notebooks vendidos: {total_notebooks}")
print(f"Vendedor que mais vendeu: {maior_vendedor['vendedor']} ({total_itens_vendedor} itens)")
print("Totais de cada produto:")
for produto, total in totais_produtos.items():
    print(f"  {produto}: {total}")


#Exercício 6 – Classificação de produtos por preço
#produtos = [
# {"nome": "Notebook", "preco": 3500},
# {"nome": "Mouse", "preco": 80},
# {"nome": "Teclado", "preco": 150},
# {"nome": "Cadeira", "preco": 900},]

# Percorra a lista de produtos com um for e classifique cada produto como:
# - 'barato' se o preço for até 100
# - 'médio' se estiver entre 101 e 1000
# - 'caro' se for acima de 1000
# Crie um novo dicionário com as classificações.


produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse",    "preco": 80},
    {"nome": "Teclado",  "preco": 150},
    {"nome": "Cadeira",  "preco": 900},
]

classificacoes = {} 

for p in produtos:
    preco = p["preco"]
    if preco <= 100:
        classe = "barato"
    elif preco <= 1000:       
        classe = "médio"
    else:
        classe = "caro"
    classificacoes[p["nome"]] = classe

print("Classificações:", classificacoes)


# Exercício 7 – Avaliação de desempenho de funcionários
# funcionarios = [
 # {"nome": "Ana", "nota": 9},
 # {"nome": "Carlos", "nota": 6},
 # {"nome": "Beatriz", "nota": 4}, 
#{"nome": "João", "nota": 7},]

# Use um for para percorrer a lista e atribua a cada funcionário:
# - 'Excelente' se nota >= 8
# - 'Regular' se nota entre 5 e 7
# - 'Precisa melhorar' se nota < 5
# Crie um novo dicionário com nome e classificação.


funcionarios = [
    {"nome": "Ana", "nota": 9},
    {"nome": "Carlos", "nota": 6},
    {"nome": "Beatriz", "nota": 4},
    {"nome": "João", "nota": 7},
]

avaliacoes = {}

for f in funcionarios:
    nota = f["nota"]
    if nota >= 8:
        classificacao = "Excelente"
    elif nota >= 5:
        classificacao = "Regular"
    else:
        classificacao = "Precisa melhorar"
    
    avaliacoes[f["nome"]] = classificacao

print("Avaliação dos funcionários:")
for nome, classe in avaliacoes.items():
    print(f"{nome}: {classe}")


# Exercício 8 – Controle de estoque com alerta
# estoque = {
 # "notebook": 3,
 # "mouse": 25,
 # "teclado": 8,
 # "monitor": 2}

# Percorra o dicionário com um for e use if/elif/else para imprimir mensagens:
# - 'Estoque crítico' se quantidade < 5
# - 'Estoque baixo' se 5 <= quantidade < 10
# - 'Estoque adequado' se quantidade >= 10


estoque = {
    "notebook": 3,
    "mouse": 25,
    "teclado": 8,
    "monitor": 2
}

for produto, quantidade in estoque.items():
    if quantidade < 5:
        status = "Estoque crítico"
    elif quantidade < 10:
        status = "Estoque baixo"
    else:
        status = "Estoque adequado"
    
    print(f"{produto.capitalize()}: {status} ({quantidade} unidades)")


# Exercício 9 – Análise de vendas por região
# vendas = [
 # {"regiao": "Sul", "valor": 12000},
 # {"regiao": "Norte", "valor": 8000},
 # {"regiao": "Sudeste", "valor": 20000},
 # {"regiao": "Centro-Oeste", "valor": 5000},]

# Use for e if/else para classificar cada região:
# - 'Meta atingida' se valor >= 10000
# - 'Meta não atingida' se valor < 10000
# Monte uma lista de dicionários com região e situação.

vendas = [
    {"regiao": "Sul", "valor": 12000},
    {"regiao": "Norte", "valor": 8000},
    {"regiao": "Sudeste", "valor": 20000},
    {"regiao": "Centro-Oeste", "valor": 5000},
]


analise = []  

for v in vendas:
    if v["valor"] >= 10000:
        situacao = "Meta atingida"
    else:
        situacao = "Meta não atingida"
    
    analise.append({
        "regiao": v["regiao"],
        "situacao": situacao
    })

print("Análise de vendas por região:")
for item in analise:
    print(f"{item['regiao']}: {item['situacao']}")


# Exercício 10 – Cálculo de desconto em compras
# compras = [
 # {"cliente": "Maria", "valor": 450},
 # {"cliente": "José", "valor": 1200},
 # {"cliente": "Clara", "valor": 3000},]

# Percorra a lista com for e aplique descontos:
# - 5% se valor < 500
# - 10% se 500 <= valor < 2000
# - 15% se valor >= 2000
# Crie um novo dicionário com cliente, valor original, desconto e valor final.


compras = [
    {"cliente": "Maria", "valor": 450},
    {"cliente": "José", "valor": 1200},
    {"cliente": "Clara", "valor": 3000},
]

resultado = []  

for c in compras:
    valor = c["valor"]
    
    if valor < 500:
        desconto = 0.05
    elif valor < 2000:
        desconto = 0.10
    else:
        desconto = 0.15
    
    valor_final = valor * (1 - desconto)
    
    resultado.append({
        "cliente": c["cliente"],
        "valor_original": valor,
        "desconto": f"{desconto * 100:.0f}%",
        "valor_final": round(valor_final, 2)
    })

print("Resumo de compras com descontos:")
for r in resultado:
    print(f"{r['cliente']}: Valor original = R$ {r['valor_original']:.2f}, "
          f"Desconto = {r['desconto']}, Valor final = R$ {r['valor_final']:.2f}")




