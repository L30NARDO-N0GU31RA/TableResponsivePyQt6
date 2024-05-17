import random

# Criação da lista de dados
dados = []

# Cabeçalho
dados.append("id pedido,linha de montagem,modelo,qtt produzida,status")

# Geração de dados para cada linha
for id_pedido in range(101):
    linha_de_montagem = random.choice(["1", "2", "3"])
    modelo = random.choice(["tradizionale", "disegno", "colori", "stone", "wordline"])
    qtt_produzida = random.randint(1, 100)
    status = random.choice(["em aberto", "em producao", "em separacao", "em transito", "entregue", "cancelado"])

    # Adiciona os dados formatados à lista
    dados.append(f"{id_pedido},{linha_de_montagem},{modelo},{qtt_produzida},{status}")

# Convertendo a lista de strings em uma única string, separada por novas linhas
dados_formatados = "\n".join(dados)

# Exibindo os dados formatados
print(dados_formatados)