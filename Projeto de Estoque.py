estoque = {}

def entrada_produto(produto, quantidade, qualidade, valor):
    if produto not in estoque:
        estoque[produto] = {"quantidade": 0, "valor_total": 0, "qualidade_total": 0}
    estoque[produto]["quantidade"] += quantidade
    estoque[produto]["valor_total"] += valor
    estoque[produto]["qualidade_total"] += qualidade

def saida_produto(produto, quantidade):
    if produto in estoque and estoque[produto]["quantidade"] >= quantidade:
        estoque[produto]["quantidade"] -= quantidade
        return True
    return False

def porcentagem_ganho_perda():
    total_valor_compra = 0
    total_valor_venda = 0
    for produto, dados in estoque.items():
        total_valor_compra += dados["valor_total"]
        total_valor_venda += (dados["valor_total"] / dados["quantidade"]) * (dados["quantidade"] - dados["quantidade_vendida"])
    if total_valor_compra > 0:
        return ((total_valor_venda - total_valor_compra) / total_valor_compra) * 100
    return 0