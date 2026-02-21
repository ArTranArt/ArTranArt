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

    # 2. Barre de progression
    bar = "█" * int(percent / 5) + "░" * (20 - int(percent / 5))
    
    # 3. Le mot magique (Placeholder)
    tag = "%PROGRESS%"
    
    # 4. Le nouveau contenu (qui remet le tag à la fin pour demain !)
    content_to_insert = (
        f"### 🗓️ {year} Year Progress\n"
        f"`{bar}` {percent:.2f}%\n\n"
        f"⏳ **{days_left}** days left until {year + 1}!\n\n"
        f"{tag}"
    )

    # 5. Lecture du README
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
            
        # 6. Remplacement UNIQUE
        if tag in content:
            # On remplace %PROGRESS% par la barre + le nouveau %PROGRESS%
            new_content = content.replace(tag, content_to_insert, 1)
            
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ Succès ! Progression mise à jour à {percent:.2f}%")
        else:
            print("⚠️ Le tag %PROGRESS% est introuvable. Rien n'a été modifié.")
            
    except FileNotFoundError:
        print("❌ Fichier README.md introuvable.")

if __name__ == "__main__":
    update_year_progress()