# Gestionnaire de Plantes 
#Par Victor - Novembre 2025
# Projet d'apprentissage Python - Session 4 

def afficher_menu():
    """Affiche le menu principal"""

    print("\n=== Gestionnaire de Plantes ===")
    print("1. Ajtouer une plante")
    print("2. Voir mes plantes")
    print("3. Quitter")

def ajouter_plante(plantes):
    """Ajoute une plante à la liste"""

    nom = input("Nom de la plante :")
    espece = input("Espece :")
    zone = input("Zone (Ile de France) : ")

    plante = {
        "nom": nom,
        "espece": espece,
        "zone": zone
    }

    plantes.append(plante)
    print(f"✅ {nom} ajoutée !")


def afficher_plantes(plantes):
    """Affiche toutes les plantes"""
    if not plantes:
        print("Aucune plante enregistrée.")
        return
    
    print("\n=== Mes Plantes ===")
    for i, plante in enumerate(plantes, 1):
        print(f"{I}. {plante['nom']} ({plante['espece']}) - Zone : {plante['zone']}")


def main():
    """Fonction principale"""
    plantes = []

    while True:
        afficher_menu()
        choix = input("\nVotre choix :")

        if choix == "1":
            ajouter_plante(plantes)
        elif choix == "2":
            afficher_plantes(plantes)
        elif choix == "3":
            print("A bientôt ! 🌱")
            break
        else:
            print("❌ Choix invalide !")


if __name__ == "__main__":
    main()