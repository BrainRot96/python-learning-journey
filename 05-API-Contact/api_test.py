import anthropic

# Ta clé API (remplace par ta vraie clé)
API_KEY = "VOTRE_CLE_ICI"

# Créer le client
client = anthropic.Anthropic(api_key=API_KEY)

# Envoyer une requête simple
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Dis bonjour en une phrase !"}
    ]
)

# Afficher la réponse
print(message.content[0].text)