import anthropic

client = anthropic.Anthropic()

resposta = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "Explique em 2 frases o que é um offset no Kafka."}],
)

print(resposta.content[0].text)
print("entrada:", resposta.usage.input_tokens, " | saída:", resposta.usage.output_tokens)