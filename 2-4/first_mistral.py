from mistralai.client import Mistral

client = Mistral(api_key="4j8baJA1xVzUhOYNDJKJokmKxzfwazZR")

response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {"role": "user", "content": "Привет! Напиши кратко, что такое FastAPI."}
    ],
    temperature=0.2,
    max_tokens=100
)

print(response.choices[0].message.content)