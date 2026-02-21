import datetime
import re

def generate_progress_bar(percent, width=20):
    """Génère une barre de progression visuelle en caractères ASCII."""
    filled_chars = int(percent / (100 / width))
    bar = "█" * filled_chars + "░" * (width - filled_chars)
    return f"`{bar}` {percent:.2f}%"

def update_year_progress():
    today = datetime.datetime.now()
    year = today.year
    
    # Calcul de la progression précise
    start_of_year = datetime.datetime(year, 1, 1)
    next_year = datetime.datetime(year + 1, 1, 1)
    
    total_seconds_year = (next_year - start_of_year).total_seconds()
    elapsed_seconds = (today - start_of_year).total_seconds()
    percent = (elapsed_seconds / total_seconds_year) * 100
    days_left = (next_year - today).days

    # Préparation du contenu dynamique
    bar_display = generate_progress_bar(percent)
    # On reste en anglais pour la cohérence de ton profil
    message = f"### 🗓️ {year} Year Progress\n{bar_display}\n\n⏳ **{days_left}** days left until {year + 1}!"

    # Lecture du README
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    # Utilisation de balises HTML invisibles pour cibler l'endroit exact de l'update
    pattern = r"()(.*?)()"
    replacement = f"\\1\n\n{message}\n\n\\3"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"✅ README mis à jour : {percent:.2f}% (Année {year})")

if __name__ == "__main__":
    update_year_progress()