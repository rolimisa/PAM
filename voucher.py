import pandas as pd
from collections import Counter

# Dados variados por cliente
dados_pedidos = pd.DataFrame([
    {'cliente_id': 1, 'pedido_id': 101, 'itens': ['sushi', 'chá verde']},
    {'cliente_id': 1, 'pedido_id': 102, 'itens': ['hamburguer artesanal', 'batata frita']},
    {'cliente_id': 1, 'pedido_id': 103, 'itens': ['macarrão ao molho branco', 'vinho']},
    {'cliente_id': 1, 'pedido_id': 104, 'itens': ['temaki', 'refrigerante']},
    {'cliente_id': 1, 'pedido_id': 105, 'itens': ['pizza calabresa', 'milkshake']},
    
    {'cliente_id': 2, 'pedido_id': 201, 'itens': ['hamburguer vegetariano', 'água']},
    {'cliente_id': 2, 'pedido_id': 202, 'itens': ['sushi', 'suco detox']},
    {'cliente_id': 2, 'pedido_id': 203, 'itens': ['lasanha', 'chá verde']},
    {'cliente_id': 2, 'pedido_id': 204, 'itens': ['batata frita', 'hamburguer artesanal']},
    {'cliente_id': 2, 'pedido_id': 205, 'itens': ['yakisoba', 'refrigerante']},
    
    {'cliente_id': 3, 'pedido_id': 301, 'itens': ['quinoa', 'legumes assados']},
    {'cliente_id': 3, 'pedido_id': 302, 'itens': ['sashimi', 'suco de uva']},
    {'cliente_id': 3, 'pedido_id': 303, 'itens': ['nhoque', 'vinho']},
    {'cliente_id': 3, 'pedido_id': 304, 'itens': ['sushi', 'chá verde']},
    {'cliente_id': 3, 'pedido_id': 305, 'itens': ['hamburguer artesanal', 'batata doce']},
    
    {'cliente_id': 4, 'pedido_id': 401, 'itens': ['lasanha', 'suco de uva']},
    {'cliente_id': 4, 'pedido_id': 402, 'itens': ['sopa de legumes', 'suco detox']},
    {'cliente_id': 4, 'pedido_id': 403, 'itens': ['sushi', 'hamburguer vegetariano']},
    {'cliente_id': 4, 'pedido_id': 404, 'itens': ['macarrão ao molho vermelho', 'vinho']},
    {'cliente_id': 4, 'pedido_id': 405, 'itens': ['pizza calabresa', 'refrigerante']},
])

# Agrupar e processar
agrupado = dados_pedidos.groupby('cliente_id')['itens'].sum().reset_index()

def item_mais_comprado(lista_itens):
    contagem = Counter(lista_itens)
    return contagem.most_common(1)[0][0]

agrupado['item_mais_comprado'] = agrupado['itens'].apply(item_mais_comprado)
agrupado['recomendacao_voucher'] = agrupado.apply(
    lambda row: f"Cliente {row['cliente_id']} comprou mais '{row['item_mais_comprado']}', por isso receberá um voucher promocional para esse item.",
    axis=1
)

# Exportar para Excel
agrupado[['cliente_id', 'item_mais_comprado', 'recomendacao_voucher']].to_excel("vouchers_clientes.xlsx", index=False)
print("\nArquivo 'vouchers_clientes.xlsx' criado com sucesso!")
