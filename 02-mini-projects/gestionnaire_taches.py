# Gestionnaire de tâches
# Victor - Session 11 - Consolidation

import json  #Création d'un fichier JSON (JavaScript Object Notation) = Format texte pour stocker des données
             #Ajouter des capacités au fichier JSON

def sauvegarder_taches(taches):
    """Sauvegarde les tâches dans un fichier JSON"""
    with open("taches.json", "w", encoding="utf-8") as fichier:
        json.dump(taches, fichier, indent=4, ensure_ascii=False)
    print("💾 Tâches sauvegardées !")

def charger_taches():
    """Charge les tâches depuis le fichier JSON"""
    try:
        with open("taches.json", "r", encoding="utf-8") as fichier:
            taches = json.load(fichier)
            print(f"📂 {len(taches)} tâche(s) chargée(s) !")
            return taches
    except FileNotFoundError:
        print("📝 Nouveau fichier créé")
        return []



def sauvegarder_taches(taches):
    """Sauvegarde les tâches dans un fichier JSON"""
    with open("taches.json", "w", encoding="utf-8") as fichier:
        json.dump(taches, fichier, indent=4, ensure_ascii=False)
    print("💾 Tâches sauvegardées !")


def charger_taches():
    """Charge les tâches depuis le fichier JSON"""
    try:
        with open("taches.json", "r", encoding="utf-8") as fichier:
            taches = json.load(fichier)
            print(f"📂 {len(taches)} tâche(s) chargée(s) !")
            return taches
    except FileNotFoundError:
        print("📝 Nouveau fichier créé")
        return []


def afficher_menu():
    """Affiche le menu principal"""

    print("\n=== GESTIONNAIRE DE TACHES ===")
    print("1 - Ajouter une tâche :")
    print("2 - Voir mes tâches :")
    print("3 - Marquer terminée")
    print("4 - Statisitiques")
    print("5 - Quitter")

def ajouter_tache(taches):
    """Demande info et ajoute tâche"""
    print("\n--- Ajouter une tâche ---")

    #Demande info :
    nom = input("Nom de la tâche :")
    priorite = input("Priorité : (Haute/Moyenne/Basse): ")

    #Créer le dictionnaire 

    tache = {
        "nom": nom,
        "priorite": priorite,
        "terminee": False
    }

    #Ajouter à la liste :
    taches.append(tache)
    print(f"✅ Tâche '{nom}' ajoutée !")

def afficher_taches(taches):
    """Afficher toutes les tâches"""

    print("\n--- Afficher les tâches ---")

    #Afficher les tâches en cours :

    
    #Dans le cas présent, il faut utiliser return tout de suite pour cloturer la boucle,
    #Si la boucle n'est pas cloturé, cela va provoqué un blocage avec la fonction suivante : "Afficher les taches"
    

    if not taches:
        print("Aucune tâche en cours")
        return
    


#Dans le cas suivant il faut créer une autre boucle 
 
    print("\n=== MES TÂCHES ===")

#Dans le cas suivant il faut afficher toutes les taches :
    for i, tache in enumerate(taches, 1):
    #Donc la on affiche toutes les taches avec cette compréhension la 

     statut = "✅" if tache["terminee"] else "⏳"
    print(f"{i}. {statut} {tache['nom']} - Priorité: {tache['priorite']}")


def marque_termine(taches):
    """Marque une tâche comme terminée"""

    print("\n--- Marquer terminée ---")

    #1 - On vérifie si la liste est vide 
    if not taches:
        print("Aucune tâche a marquer")
        return
    
    afficher_taches(taches) #La on réutilise la fonction
    numero = int(input("\nNuméro de la tâche :")) #On demande le numéro de la tache 

    taches[numero - 1]["terminee"] = True # la on change dans le dictionnaire 
    print(f"✅ Tâche {numero} marquée terminée !")


def afficher_stats(taches):
    print("\n--- Statistiques ---")

    #Total : 
    total = len(taches)

    #terminée (les taches) --> compréhension 

    terminees = [t for t in taches if t["terminee"]]
    nb_terminees = len(terminees)

    #Ensuite ce sont les taches en cours : 

    en_cours = total - nb_terminees

    #affiché les taches 

    print(f"📊 Total : {total} tâches")
    print(f"✅ Terminées : {nb_terminees}")
    print(f"⏳ En cours : {en_cours}")

def main():
    """Fonction principale"""
    taches = charger_taches()  # ← NOUVEAU : Charge au démarrage
    
    while True:
        afficher_menu()
        choix = input("\nVotre choix : ")
        
        if choix == "1":
            ajouter_tache(taches)
            sauvegarder_taches(taches)  # ← NOUVEAU : Sauvegarde
            
        elif choix == "2":
            afficher_taches(taches)
            
        elif choix == "3":
            marquer_terminee(taches)
            sauvegarder_taches(taches)  # ← NOUVEAU : Sauvegarde
            
        elif choix == "4":
            afficher_stats(taches)
            
        elif choix == "5":
            sauvegarder_taches(taches)  # ← NOUVEAU : Sauvegarde finale
            print("Au revoir ! 👋")
            break
            
        else:
            print("❌ Choix invalide !")

if __name__ == "__main__":
    main()

# --------------------- JSON -------------------------

def sauvegarder_tache(taches):
    """Sauvegarder les taches dans un fichier JSON""" 

    #Ouvrir / Créer fichier en mode écriture
    with open("taches.json", "w", encoding = "utf-8") as fichier:
        json.dump(taches, fichier, indent=4, ensure_ascii=False)

    print("💾 Tâches sauvegardées !")


#open() ---> Ouvre / créer fichier si existe pas, le nomme
#w = write 
#UTF-8 = accent français 
# as fichier = nom de variable
# with = gestion automatique, cela ferme le fichier après


                  








