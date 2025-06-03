from datetime import datetime, timedelta

# Base fictícia de entregas de fornecedores
entregas_fornecedores = {
    "F001": {
        "fornecedor": "Fornecedor A",
        "produto": "Carne bovina",
        "status": "Em atraso",
        "entrega_prevista": datetime.now() + timedelta(hours=-2)
    },
    "F002": {
        "fornecedor": "Fornecedor B",
        "produto": "Pão de hambúrguer",
        "status": "Entregue",
        "entrega_prevista": datetime.now()
    },
    "F003": {
        "fornecedor": "Fornecedor C",
        "produto": "Refrigerante",
        "status": "Em rota",
        "entrega_prevista": datetime.now() + timedelta(hours=1)
    },
}

# Base fictícia de pedidos de clientes
pedidos_clientes = {
    "12345": {
        "cliente": "Ana",
        "status": "Saiu para entrega",
        "horario_previsto": datetime.now() + timedelta(minutes=30)
    },
    "67890": {
        "cliente": "Carlos",
        "status": "Preparando pedido",
        "horario_previsto": datetime.now() + timedelta(minutes=45)
    },
    "11111": {
        "cliente": "João",
        "status": "Pedido recebido",
        "horario_previsto": datetime.now() + timedelta(minutes=60)
    },
    "22222": {
        "cliente": "Ana",
        "status": "Entregue",
        "horario_previsto": datetime.now() - timedelta(minutes=20)
    }
}

# Função que interpreta perguntas
def responder_pergunta(pergunta):
    pergunta = pergunta.lower()

    # 1. Fornecedores atrasados
    if "fornecedor" in pergunta and "atrasado" in pergunta:
        respostas = []
        for f in entregas_fornecedores.values():
            if f["status"] == "Em atraso":
                respostas.append(
                    f"{f['fornecedor']} está atrasado com {f['produto']}, previsto para {f['entrega_prevista'].strftime('%H:%M')}."
                )
        return "\n".join(respostas) if respostas else "Nenhum fornecedor está atrasado."

    # 2. Status de pedido por código
    elif "pedido" in pergunta and any(c in pergunta for c in pedidos_clientes):
        for codigo, p in pedidos_clientes.items():
            if codigo in pergunta:
                return (f"Pedido {codigo} de {p['cliente']} está com status: {p['status']}. "
                        f"Previsão de entrega: {p['horario_previsto'].strftime('%H:%M')}.")
        return "Pedido não encontrado. Verifique o código informado."

    # 3. Todos os pedidos de um cliente (com tabela)
    elif "pedidos de" in pergunta:
        partes = pergunta.split("pedidos de")
        if len(partes) > 1:
            nome_cliente = partes[1].strip().lower()

            encontrados = []
            for codigo, p in pedidos_clientes.items():
                if nome_cliente in p['cliente'].lower():
                    encontrados.append([
                        p['cliente'], codigo, p['status'], p['horario_previsto'].strftime('%H:%M')
                    ])

            if encontrados:
                resposta = "Cliente | Código | Status              | Previsão\n"
                resposta += "-" * 50 + "\n"
                for cliente, cod, status, horario in encontrados:
                    resposta += f"{cliente:<8} | {cod:<6} | {status:<18} | {horario}\n"
                return resposta
            else:
                return f"Nenhum pedido encontrado para '{nome_cliente.title()}'."
        else:
            return "Por favor, informe o nome do cliente após 'pedidos de'."

    # 4. Produtos entregues
    elif "produto entregue" in pergunta or "entregue" in pergunta:
        entregues = [f"{f['produto']} por {f['fornecedor']}" for f in entregas_fornecedores.values() if f["status"] == "Entregue"]
        return "\n".join(entregues) if entregues else "Nenhum produto foi entregue ainda."

    # 5. Quem entrega um produto
    elif "quem entrega" in pergunta:
        for f in entregas_fornecedores.values():
            if f['produto'].lower() in pergunta:
                return f"O produto {f['produto']} será entregue por {f['fornecedor']}."
        return "Não foi possível identificar o produto na base de dados."

    # 6. Relatório geral de fornecedores
    elif "status dos fornecedores" in pergunta:
        return "\n".join([f"{f['fornecedor']} ({f['produto']}): {f['status']}" for f in entregas_fornecedores.values()])

    return "Desculpe, não entendi a pergunta. Você pode perguntar sobre pedidos, fornecedores ou produtos."

# Execução
print("🤖 Chatbot Restaurante — Digite 'sair' para encerrar\n")

while True:
    entrada = input("Você: ")
    if entrada.lower() == "sair":
        break
    resposta = responder_pergunta(entrada)
    print("Bot:", resposta, "\n")
