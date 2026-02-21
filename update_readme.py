import datetime

def update_year_progress():
    # 1. Calculs
    today = datetime.datetime.now()
    year = today.year
    start = datetime.datetime(year, 1, 1)
    next_year = datetime.datetime(year + 1, 1, 1)
    
    progress = (today - start) / (next_year - start)
    percent = progress * 100
    days_left = (next_year - today).days

    # 2. Génération du texte de la barre (Style Badge SVG dynamique)
    percent_int = int(percent) # geps.dev utilise des nombres entiers
    progress_text = (
        f"Here is my homeday daytime counter before next year ⏳ **{days_left}** days left until {year + 1}. ![Year Progress](https://geps.dev/progress/{percent_int})\n\n"
    )

    # 3. Lecture du TEMPLATE (qui est toujours propre)
    try:
        with open("README_template.md", "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        print("❌ Erreur : Le fichier README_template.md n'existe pas.")
        return

    # 4. Remplacement du mot clé et création du NOUVEAU fichier
    final_readme = template.replace("{progress_bar}", progress_text)

    # 5. Écrasement total du README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(final_readme)
        
    print(f"✅ README généré à neuf avec succès : {percent:.2f}% (Badge: {percent_int}%)")

if __name__ == "__main__":
    update_year_progress()