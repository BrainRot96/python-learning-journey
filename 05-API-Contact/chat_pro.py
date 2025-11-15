import anthropic
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    print("Erreur : Cle API non trouvee")
    exit()

client = anthropic.Anthropic(api_key=API_KEY)
conversation_history = []
total_input_tokens = 0
total_output_tokens = 0

# Prix par million de tokens (approximatif pour Claude Sonnet)
PRIX_INPUT = 3.0  # euros par million
PRIX_OUTPUT = 15.0  # euros par million

print("=== Assistant IA Pro - Tape 'quit' pour quitter ===\n")

while True:
    try:
        user_input = input("Toi : ")
        
        if user_input.lower() == "quit":
            # Calculer le cout
            cout_input = (total_input_tokens / 1_000_000) * PRIX_INPUT
            cout_output = (total_output_tokens / 1_000_000) * PRIX_OUTPUT
            cout_total = cout_input + cout_output
            
            # Afficher les stats
            print(f"\n📊 Statistiques de la session :")
            print(f"   Tokens entree : {total_input_tokens}")
            print(f"   Tokens sortie : {total_output_tokens}")
            print(f"   Total tokens : {total_input_tokens + total_output_tokens}")
            print(f"\n💰 Cout estime :")
            print(f"   Entree : {cout_input:.6f} €")
            print(f"   Sortie : {cout_output:.6f} €")
            print(f"   TOTAL : {cout_total:.6f} €")
            
            # Sauvegarder la conversation
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"conversation_{timestamp}.json"
            
            conversation_data = {
                "date": datetime.now().isoformat(),
                "total_input_tokens": total_input_tokens,
                "total_output_tokens": total_output_tokens,
                "cout_total_euros": cout_total,
                "messages": conversation_history
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(conversation_data, f, ensure_ascii=False, indent=2)
            
            print(f"\n💾 Conversation sauvegardee : {filename}")
            print("\nAu revoir ! 👋")
            break
        
        conversation_history.append({"role": "user", "content": user_input})
        
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=conversation_history
        )
        
        total_input_tokens += message.usage.input_tokens
        total_output_tokens += message.usage.output_tokens
        
        assistant_response = message.content[0].text
        conversation_history.append({"role": "assistant", "content": assistant_response})
        
        # Calculer le cout de ce message
        cout_msg = ((message.usage.input_tokens / 1_000_000) * PRIX_INPUT + 
                    (message.usage.output_tokens / 1_000_000) * PRIX_OUTPUT)
        
        print(f"\nClaude : {assistant_response}")
        print(f"💰 Tokens : {message.usage.input_tokens} in / {message.usage.output_tokens} out (~{cout_msg:.6f} €)\n")
        
    except Exception as e:
        print(f"\nErreur : {e}\n")