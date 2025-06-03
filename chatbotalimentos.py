# Base de conhecimento sobre pratos e ingredientes
base_conhecimento = {
    "salada tropical": {
        "ingredientes": ["alface", "manga", "cenoura", "nozes", "molho de iogurte"],
        "beneficios": {
            "alface": "rica em fibras e ajuda na digestão",
            "manga": "fonte de vitamina C e antioxidantes",
            "cenoura": "boa para a visão, rica em betacaroteno",
            "nozes": "auxiliam na saúde do coração",
            "molho de iogurte": "fonte de probióticos que melhoram a flora intestinal"
        }
    },
    "frango grelhado com arroz integral": {
        "ingredientes": ["frango", "arroz integral", "brócolis", "azeite de oliva"],
        "beneficios": {
            "frango": "rico em proteínas magras",
            "arroz integral": "bom para o intestino e ajuda no controle glicêmico",
            "brócolis": "rico em fibras, vitaminas e minerais",
            "azeite de oliva": "rico em gorduras boas, bom para o coração"
        }
    }
}

def exibir_cardapio():
    resposta = "\n📋 Cardápio disponível:\n"
    for prato in base_conhecimento:
        resposta += f"🍽️ {prato.title()}\n"
    return resposta

def responder_usuario(pergunta):
    pergunta = pergunta.lower().strip()

    if pergunta in ["cardapio", "cardápio", "menu"]:
        return exibir_cardapio()

    for prato, dados in base_conhecimento.items():
        if prato in pergunta:
            resposta = f"\n🍽️ Prato: {prato.title()}\n"
            resposta += f"Ingredientes: {', '.join(dados['ingredientes'])}.\n"
            resposta += "🟡 Benefícios dos ingredientes:\n"
            for ing, ben in dados["beneficios"].items():
                resposta += f"👉 {ing.title()}: {ben}\n"
            return resposta

    return "Desculpe, não encontrei esse prato no nosso cardápio. Digite 'cardápio' para ver as opções disponíveis."

# Chat com o usuário
print("🤖 Chatbot Restaurante IA — Pergunte sobre os pratos e seus benefícios.")
print("💡 Comandos disponíveis: 'cardápio', nome do prato, ou 'sair' para encerrar.\n")

while True:
    entrada = input("Você: ")
    if entrada.lower() in ["sair", "exit", "quit"]:
        print("Chatbot: Até logo! 😊")
        break

    resposta = responder_usuario(entrada)
    print(f"Chatbot: {resposta}\n")
