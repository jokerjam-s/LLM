from mistralai.client import Mistral

system_prompt = "Ты — генератор JSON. Ответ должен быть строго валидным JSON с полями: 'term' (строка) и 'definition' (строка до 100 символов)."
user_prompt = "Определи термин: FastAPI"

# Ваш код здесь
client = Mistral(api_key="4j8baJA1xVzUhOYNDJKJokmKxzfwazZR")

response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    temperature=0.0,
    max_tokens=120
)

print(response.choices[0].message.content)
