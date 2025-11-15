import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    print("Erreur : clef API non trouvee")
    exit()

client = anthropic.Anthropic(api_key=API_KEY)
conversation_history = []
total_input_tokens = 0
total_output_tokens = 0

print("=== Assistant IA avec Streaming - Tape 'quit' pour quitter ===\n")


while True:
    try:
        user_input = input("Toi :")

        if user_input.lower() == "quit":
            print(f"\n📊 Statistiques :")
            print(f"   Tokens entree : {total_input_tokens}")
            print(f"   Tokens sortie : {total_output_tokens}")
            print(f"   Total : {total_input_tokens + total_output_tokens}")
            print("\nAu revoir ! 👋")
            break

        conversation_history.append({"role": "user", "content": user_input})

        print("\nClaude : ", end="", flush=True)

        full_response = ""

        with client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=conversation_history
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
                full_response += text

        print("\n")

        message = stream.get_final_message()
        total_input_tokens += message.usage.input_tokens
        total_output_tokens += message.usage.output_tokens
        
        # Ajouter la réponse complète à l'historique
        conversation_history.append({"role": "assistant", "content": full_response})
        
        print(f"💰 Tokens : {message.usage.input_tokens} in / {message.usage.output_tokens} out\n")
        
    except Exception as e:
        print(f"\nErreur : {e}\n")     
