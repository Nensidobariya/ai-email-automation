from google import genai

API_KEY = "AIzaSyByYm_q2fwBjERN-VVu8yiDcWwnQBTfG4o"
client = genai.Client(api_key=API_KEY)

def generate_email(purpose, recipient, tone, details):
    prompt = f"""
    Write a professional business email:
    Purpose: {purpose}
    Recipient: {recipient}
    Tone: {tone}
    Details: {details}
    Include: Subject line, Greeting, Body, Closing, Signature.
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt
    )
    return response.text

def main():
    print("=" * 50)
    print("  AI EMAIL AUTOMATION TOOL")
    print("  Powered by Google Gemini API")
    print("=" * 50)
    purpose = input("\n1. What is the email about?\n   > ")
    recipient = input("\n2. Who are you sending it to?\n   > ")
    tone = input("\n3. Tone? (formal/friendly/urgent)\n   > ")
    details = input("\n4. Any specific details?\n   > ")
    print("\nGenerating your email...\n")
    email = generate_email(purpose, recipient, tone, details)
    print("=" * 50)
    print("YOUR PROFESSIONAL EMAIL:")
    print("=" * 50)
    print(email)
    print("=" * 50)
    another = input("\nGenerate another? (yes/no): ")
    if another.lower() == "yes":
        main()

if __name__ == "__main__":
    main()