from datetime import datetime, timedelta
import re

# 📦 Base simulada de entregas com 10 pedidos
entregas = {
    "12345": {
        "cliente": "Ana",
        "status": "Saiu para entrega",
        "horario_previsto": datetime.now() + timedelta(minutes=30)
    },
    "67890": {
        "cliente": "Carlos",
        "status": "Preparando pedido",
        "horario_previsto": datetime.now() + timedelta(minutes=50)
    },
    "11223": {
        "cliente": "Beatriz",
        "status": "Aguardando confirmação do restaurante",
        "horario_previsto": datetime.now() + timedelta(minutes=60)
    },
    "33445": {
        "cliente": "Daniel",
        "status": "Saiu para entrega",
        "horario_previsto": datetime.now() + timedelta(minutes=25)
    },
    "55667": {
        "cliente": "Fernanda",
        "status": "Entregue",
        "horario_previsto": datetime.now() - timedelta(minutes=10)
    },
    "77889": {
        "cliente": "Eduardo",
        "status": "Cancelado pelo cliente",
        "horario_previsto": datetime.now()
    },
    "99100": {
        "cliente": "Juliana",
        "status": "Pedido recebido pelo restaurante",
        "horario_previsto": datetime.now() + timedelta(minutes=45)
    },
    "10203": {
        "cliente": "Leonardo",
        "status": "Preparando pedido",
        "horario_previsto": datetime.now() + timedelta(minutes=40)
    },
    "20405": {
        "cliente": "Marina",
        "status": "Saiu para entrega",
        "horario_previsto": datetime.now() + timedelta(minutes=15)
    },
    "30607": {
        "cliente": "Ricardo",
        "status": "Aguardando pagamento",
        "horario_previsto": datetime.now() + timedelta(minutes=70)
    }
}

# 🧠 NLP simples para extrair número do pedido e intenção
def entender_mensagem(mensagem):
    pedido_match = re.search(r'\b\d{5}\b', mensagem)
    pedido_id = pedido_match.group() if pedido_match else None

    if "cancelar" in mensagem.lower():
        intencao = "cancelamento"
    elif "status" in mensagem.lower() or "onde" in mensagem.lower() or "entrega" in mensagem.lower():
        intencao = "status"
    elif "tempo" in mensagem.lower() or "quando" in mensagem.lower():
        intencao = "tempo_estimado"
    else:
        intencao = "indefinido"

    return pedido_id, intencao

# 🤖 Lógica de resposta do bot
def responder_cliente(mensagem):
    pedido_id, intencao = entender_mensagem(mensagem)

    if not pedido_id:
        return "Por favor, informe o número do pedido (ex: 12345)."

    pedido = entregas.get(pedido_id)
    if not pedido:
        return f"Não encontrei informações para o pedido {pedido_id}."

    if intencao == "status":
        return f"O pedido {pedido_id} está atualmente com status: {pedido['status']}."
    elif intencao == "tempo_estimado":
        tempo_restante = pedido['horario_previsto'] - datetime.now()
        minutos = int(tempo_restante.total_seconds() // 60)
        if minutos < 0:
            return f"O pedido {pedido_id} já deveria ter sido entregue."
        return f"O pedido {pedido_id} deve chegar em aproximadamente {minutos} minutos."
    elif intencao == "cancelamento":
        return f"Seu pedido {pedido_id} está em andamento. Para cancelamentos, entre em contato com a central."
    else:
        return f"Desculpe, não entendi sua solicitação sobre o pedido {pedido_id}. Pode reformular?"

# 🟢 Chat interativo
print("🤖 Bem-vindo ao ChatBot de Entregas do Restaurante!")
print("Digite sua pergunta ou 'sair' para encerrar.\n")

while True:
    entrada = input("Você: ")
    if entrada.lower() in ["sair", "exit", "quit"]:
        print("🤖 Bot: Obrigado por usar nosso atendimento. Até logo!")
        break

    resposta = responder_cliente(entrada)
    print(f"🤖 Bot: {resposta}\n")

