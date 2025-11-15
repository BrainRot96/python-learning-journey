import anthropic
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    print("Erreur : Clef API non trouvee")
    exit()

client = anthropic.Anthropic(api_key=API_KEY)
conversation_history = []  # ✅ CORRIGÉ : liste vide, pas 0
total_input_tokens = 0
total_output_tokens = 0

PRIX_INPUT = 3.0
PRIX_OUTPUT = 15.0

def afficher_aide():
    """Affiche la liste des commandes disponibles"""
    print("\n📋 COMMANDES DISPONIBLES :")
    print("   /help  - Afficher cette aide")
    print("   /clear - Effacer l'historique de conversation")
    print("   /cost  - Afficher le cout actuel")
    print("   /save  - Sauvegarder la conversation maintenant")
    print("   quit   - Quitter l'assistant\n")

def afficher_cout():
    """Affiche les statistiques et le cout actuel"""
    cout_input = (total_input_tokens / 1_000_000) * PRIX_INPUT
    cout_output = (total_output_tokens / 1_000_000) * PRIX_OUTPUT
    cout_total = cout_input + cout_output

    print(f"\n💰 COUT ACTUEL :")
    print(f"   Tokens entree : {total_input_tokens}")
    print(f"   Tokens sortie : {total_output_tokens}")
    print(f"   Total tokens : {total_input_tokens + total_output_tokens}")
    print(f"   Cout estime : {cout_total:.6f} €\n")

def sauvegarder_conversation():
    """Sauvegarde la conversation dans un fichier JSON"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversation_{timestamp}.json"

    cout_total = ((total_input_tokens / 1_000_000) * PRIX_INPUT +
                  (total_output_tokens / 1_000_000) * PRIX_OUTPUT)
    
    conversation_data = {
        "date": datetime.now().isoformat(),  # ✅ CORRIGÉ : ajout des ()
        "total_input_tokens": total_input_tokens,
        "total_output_tokens": total_output_tokens,
        "cout_total_euros": cout_total,
        "messages": conversation_history  # ✅ CORRIGÉ : "messages" avec 's'
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(conversation_data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Conversation sauvegardee : {filename}\n")

def effacer_historique():
    """Efface l'historique de conversation"""
    global conversation_history, total_input_tokens, total_output_tokens
    conversation_history = []
    total_input_tokens = 0
    total_output_tokens = 0 
    print("\n🗑️  Historique efface ! Nouvelle conversation demarree.\n")

print("=== Assistant IA Avance - Tapez /help pour les commandes ===\n")
afficher_aide()

while True: 
    try:
        user_input = input("Toi : ")

        if user_input.lower() == "quit":
            afficher_cout()
            sauvegarder_conversation()
            print("Au revoir ! 👋")
            break
        
        elif user_input.lower() == "/help":
            afficher_aide()
            continue

        elif user_input.lower() == "/clear":
            effacer_historique()
            continue

        elif user_input.lower() == "/cost":
            afficher_cout()
            continue

        elif user_input.lower() == "/save":
            sauvegarder_conversation()
            continue

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

        cout_msg = ((message.usage.input_tokens / 1_000_000) * PRIX_INPUT + 
                    (message.usage.output_tokens / 1_000_000) * PRIX_OUTPUT)
        
        print(f"\nClaude : {assistant_response}")
        print(f"💰 Tokens : {message.usage.input_tokens} in / {message.usage.output_tokens} out (~{cout_msg:.6f} €)\n")
        
    except Exception as e:
        print(f"\nErreur : {e}\n")