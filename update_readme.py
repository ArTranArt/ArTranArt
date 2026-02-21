import datetime

def generate_progress_bar(percent, width=20):
    filled_chars = int(percent / (100 / width))
    bar = "█" * filled_chars + "░" * (width - filled_chars)
    return f"`{bar}` {percent:.2f}%"

def update_year_progress():
    today = datetime.datetime.now()
    year = today.year
    start_of_year = datetime.datetime(year, 1, 1)
    next_year = datetime.datetime(year + 1, 1, 1)
    
    progress = (today - start_of_year) / (next_year - start_of_year)
    percent = progress * 100
    days_left = (next_year - today).days

    # Le contenu à insérer (SANS les balises START/END)
    message = f"### 🗓️ {year} Year Progress\n{generate_progress_bar(percent)}\n\n⏳ **{days_left}** days left until {year + 1}!"

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # On découpe le fichier proprement
    start_tag = ""
    end_tag = ""
    
    try:
        before = content.split(start_tag)[0]
        after = content.split(end_tag)[1]
        
        # On reconstruit le fichier : AVANT + BALISE_DEBUT + MESSAGE + BALISE_FIN + APRES
        new_content = f"{before}{start_tag}\n\n{message}\n\n{end_tag}{after}"

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ README mis à jour proprement.")
    except IndexError:
        print("❌ Erreur : Balises introuvables dans le README.md")

if __name__ == "__main__":
    update_year_progress()