import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from transformers import pipeline

# Baixar stopwords do português
nltk.download('stopwords')
stop_words = stopwords.words('portuguese')

# Histórico de pedidos simulados
dados_clientes = pd.DataFrame({
    'cliente_id': [1, 2, 3, 4, 5],
    'historico_pedidos': [
        "hamburguer artesanal, batata frita, coca-cola",
        "pizza calabresa, suco de laranja",
        "hamburguer duplo, batata frita, milkshake",
        "macarrão ao molho branco, vinho",
        "sushi, sashimi, chá verde"
    ]
})

# TF-IDF com filtro de palavras comuns em português
vetorizador = TfidfVectorizer(stop_words=stop_words)
vetores = vetorizador.fit_transform(dados_clientes['historico_pedidos'])

# Agrupamento (padrões de comportamento)
kmeans = KMeans(n_clusters=2, random_state=42)
dados_clientes['grupo'] = kmeans.fit_predict(vetores)

# LLM - Gerador de texto com GPT-2
gerador = pipeline("text-generation", model="gpt2")

def gerar_sugestao_voucher(historico):
    prompt = f"O cliente costuma pedir: {historico}. Qual prato e desconto devemos sugerir?"
    resultado = gerador(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
    return resultado

# Aplicar sugestão a cada cliente
dados_clientes['sugestao_voucher'] = dados_clientes['historico_pedidos'].apply(gerar_sugestao_voucher)

# Exibir resultado final
print(dados_clientes[['cliente_id', 'historico_pedidos', 'grupo', 'sugestao_voucher']])
