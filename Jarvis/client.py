from google import genai

client = genai.Client(api_key="Enter the API key here")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is AI and ML"
)

print(response.text)
