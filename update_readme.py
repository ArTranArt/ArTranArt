import datetime

def update_year_progress():
    # 1. Calculs
    today = datetime.datetime.now()
    year = today.year
    start = datetime.datetime(year, 1, 1)
    end = datetime.datetime(year + 1, 1, 1)
    progress = (today - start) / (end - start)
    percent = progress * 100
    days_left = (end - today).days

    # 2. Barre de progression
    width = 20
    filled = int(percent / (100 / width))
    bar = "█" * filled + "░" * (width - filled)
    
    # 3. Le bloc complet
    start_tag = ""
    end_tag = ""
    
    content_to_insert = (
        f"{start_tag}\n"
        f"### 🗓️ {year} Year Progress\n"
        f"`{bar}` {percent:.2f}%\n\n"
        f"⏳ **{days_left}** days left until {year + 1}!\n"
        f"{end_tag}"
    )

    # 4. Lecture et Remplacement
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Si les balises existent, on remplace tout le bloc (balises incluses)
    if start_tag in readme_content and end_tag in readme_content:
        import re
        # On utilise une regex simple pour remplacer tout ce qui est entre les balises, balises incluses
        pattern = f"{start_tag}.*?{end_tag}"
        new_content = re.sub(pattern, content_to_insert, readme_content, flags=re.DOTALL)
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Success! Progress: {percent:.2f}%")
    else:
        print("❌ Error: Tags not found in README.md")

if __name__ == "__main__":
    update_year_progress()