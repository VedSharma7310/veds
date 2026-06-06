from google import genai

client = genai.Client(api_key="AQ.Ab8RN6Ke_VvEjTmK8AqQzMA1VxHB0g9wDeT6e3bUyyNaiHB2gA")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is AI and ML"
)

print(response.text)