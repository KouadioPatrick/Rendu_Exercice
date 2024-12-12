import random
regions = {
    "Cavally": "Guiglo",
    "Guémon": "Duékoué",
    "Tonkpi": "Man",
    "Gbôklé": "Sassandra",
    "Nawa": "Soubré",
    "San Pedro": "San Pédro",
    "Gôh": "Gagnoa",
    "Lôh-Djiboua": "Divo",
    "Bélier": "Toumodi",
    "Ifou": "Daoukro",
    "Moronou": "Bongouanou",
    "Agnéby-Tiassa": "Agboville",
    "La Mé": "Adzopé",
    "Grands-Ponts": "Dabou",
    "Bagoué": "Boundiali",
    "Poro": "Korhogo",
    "Tchologo": "Ferkessédougou",
    "Bafing": "Touba",
    "Béré": "Mankono",
    "Worodougou": "Séguéla",
    "Gbêkê": "Bouaké",
    "Hambol": "Katiola",
    "Bounkani": "Bouna",
    "Gontougo": "Bondoukou",
    "Kabadougou": "Odienné",
    "Folon": "Minignan",
    "Haut-Sassandra": "Daloa",
    "Marahoué": "Bouaflé",
    "Sud-Comoé": "Aboisso",
    "Indénié-Djuablin": "Abengourou"
}
top_scores = []
def appreciation(score):
    if score >= 9:
        return "Excellent ! Tu es gbè ! On peut t'appeler professeur des chefs-lieux, tu gères.  "
    elif score >= 7:
        return "Très bien ! Ah, tu es bon dedans, mais faut encore pousser pour devenir ministre du découpage."
    elif score >= 5:
        return "Bon travail ! Tu es dedans, mais faut pas dormir sur ça, revise un peu encore."
    elif score >= 3:
        return "Passable ! Mon frère, tu es sur la touche. Si c’était un match, coach allait te changer déjà."
    else:
        return "Insuffisant ! Ton niveau est comme  un Wi-Fi coupé. Faut aller te connecter djo !"



def play_game():
    global top_scores
    questions = random.sample(list(regions.items()), min(10, len(regions)))  # 10 questions max
    score = 0

    print("\n=== Début de la partie ===")
    for i, (region, chef_lieu) in enumerate(questions, start=1):
        print(f"Question {i}: Quel est le chef-lieu de la région {region}?")
        reponse = input("Votre réponse: ").strip()

        if reponse.lower() == chef_lieu.lower():
            print("Bonne réponse!")
            score += 1
        else:
            print(f"Mauvaise réponse. La bonne réponse est : {chef_lieu}")

    print(f"\nFin de la partie. Votre score: {score}/10")
    print("Appréciation :", appreciation(score))

    if len(top_scores) < 5 or score > min(top_scores):
        if len(top_scores) == 5:
            top_scores.remove(min(top_scores))  # Retirer le plus bas score
        top_scores.append(score)
        top_scores.sort(reverse=True)  # Trier les scores par ordre décroissant

    print("\n=== Classement actuel ===")
    for idx, top_score in enumerate(top_scores, start=1):
        print(f"{idx}. {top_score}/10")
    print()


def main():
    while True:
        print("\n=== Bienvenue dans le jeu des régions de Côte d'Ivoire ===")
        print("Les 5 meilleurs scores actuels :")
        if top_scores:
            for idx, score in enumerate(top_scores, start=1):
                print(f"{idx}. {score}/10")
        else:
            print("Aucun score pour le moment.")

        play_game()

        rejouer = input("Voulez-vous jouer une autre partie? (O/N): ").strip().upper()
        if rejouer != 'O':
            print("Merci d'avoir joué! À bientôt!")
            break


if __name__ == "__main__":
    main()
