from google import genai

# Initialize client
client = genai.Client(
    api_key="AIzaSyAMLdBe-D32Mlp0xwIzOAHqesKkfqG-VkQ"
)

def generate_summary(stock, sentiment):

    prompt = f"""
    Analyze stock {stock}.

    Market sentiment is {sentiment}.

    Give a short professional investment insight.
    """

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

    return response.text


# Test
summary = generate_summary(
    "AAPL",
    "Positive"
)

print(summary)
