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
    
    # 3. Préparation du bloc
    start_tag = ""
    end_tag = ""
    new_content = (
        f"### 🗓️ {year} Year Progress\n"
        f"`{bar}` {percent:.2f}%\n\n"
        f"⏳ **{days_left}** days left until {year + 1}!"
    )

    # 4. Reconstruction du fichier
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    final_lines = []
    skip = False
    
    for line in lines:
        if start_tag in line:
            final_lines.append(line) # Garde la balise de début
            final_lines.append(f"\n{new_content}\n\n") # Insère le contenu
            skip = True # Ignore tout ce qu'il y avait avant jusqu'à la fin
        elif end_tag in line:
            final_lines.append(line) # Garde la balise de fin
            skip = False
        elif not skip:
            final_lines.append(line)

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(final_lines)

if __name__ == "__main__":
    update_year_progress()