import anthropic

# Ta clé API
API_KEY = "***REMOVED***"

# Créer le client
client = anthropic.Anthropic(api_key=API_KEY)

# Historique de la conversation
conversation_history = []

print("=== Assistant IA - Tape 'quit' pour quitter ===\n")

# Boucle de conversation
while True:
    # Demander à l'utilisateur
    user_input = input("Toi : ")
    
    # Quitter si demandé
    if user_input.lower() == "quit":
        print("Au revoir !")
        break
    
    # Ajouter le message de l'utilisateur à l'historique
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    # Envoyer à Claude
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=conversation_history
    )
    
    # Récupérer la réponse
    assistant_response = message.content[0].text
    
    # Ajouter la réponse à l'historique
    conversation_history.append({
        "role": "assistant",
        "content": assistant_response
    })
    
    # Afficher la réponse
    print(f"\nClaude : {assistant_response}\n")