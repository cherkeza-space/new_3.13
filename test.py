from api import API_KEY
from openai import OpenAI

client = OpenAI(api_key=API_KEY)
prompt = "რომელი წელი არის ახლა?"

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=50
    )
    
    print("FULL RESPONSE:", response) 
    text = response.choices[0].message.content if response.choices[0].message else "Response is empty"

except Exception as e:
    text = f"შეცდომა: {str(e)}"

print("FINAL TEXT:", text)