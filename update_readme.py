import datetime
import re

def update_year_progress():
    # 1. Calculs
    today = datetime.datetime.now()
    year = today.year
    start = datetime.datetime(year, 1, 1)
    next_year = datetime.datetime(year + 1, 1, 1)
    
    progress = (today - start) / (next_year - start)
    percent = progress * 100
    days_left = (next_year - today).days

    # 2. Génération de la barre
    bar = "█" * int(percent / 5) + "░" * (20 - int(percent / 5))
    
    # 3. Le NOUVEAU bloc (qui contient les balises pour pouvoir être remplacé demain)
    new_block = (
        "\n"
        f"### 🗓️ {year} Year Progress\n"
        f"`{bar}` {percent:.2f}%\n\n"
        f"⏳ **{days_left}** days left until {year + 1}!\n"
        ""
    )

    # 4. Lecture
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # 5. Remplacement dynamique (écrase l'ancien bloc par le nouveau)
    # Le re.DOTALL est la magie qui permet de sélectionner sur plusieurs lignes
    new_content = re.sub(
        r".*?", 
        new_block, 
        content, 
        flags=re.DOTALL
    )

    # 6. Sauvegarde
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"✅ Mise à jour dynamique réussie : {percent:.2f}%")

if __name__ == "__main__":
    update_year_progress()