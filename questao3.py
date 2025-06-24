import openai
import os

# Configurar a API Key da OpenAI
openai.api_key = "SUA_CHAVE_API_AQUI"

# Função para gerar resposta automática
def gerar_resposta_ia(pergunta_cliente):
    prompt = f"""
Você é um atendente de suporte ao cliente de uma loja online.
Responda de forma educada, objetiva e clara a seguinte mensagem recebida de um cliente:

Mensagem do cliente:
\"\"\"{pergunta_cliente}\"\"\"

Resposta:
"""
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4o",  # pode mudar pra gpt-3.5-turbo se quiser
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        texto_resposta = resposta.choices[0].message.content.strip()
        return texto_resposta

    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return None

# Exemplo de lista de mensagens de clientes
mensagens_clientes = [
    "Meu pedido ainda não chegou, já faz mais de 10 dias!",
    "Quero trocar o tamanho da camiseta que comprei.",
    "Como faço para cancelar meu pedido?",
]

# Processar todas as mensagens
for i, msg in enumerate(mensagens_clientes):
    print(f"\n🔔 Processando mensagem {i+1}: {msg}")
    resposta = gerar_resposta_ia(msg)
    if resposta:
        nome_arquivo = f"resposta_cliente_{i+1}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"Pergunta do cliente:\n{msg}\n\nResposta gerada:\n{resposta}")
        print(f"✅ Resposta salva no arquivo: {nome_arquivo}")
    else:
        print("❌ Falha ao gerar a resposta.")

print("\n✅ Automação de IA concluída!")
