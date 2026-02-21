import datetime
import re

def generate_progress_bar(percent, width=20):
    filled_chars = int(percent / (100 / width))
    bar = "█" * filled_chars + "░" * (width - filled_chars)
    return f"`{bar}` {percent:.2f}%"

def update_year_progress():
    today = datetime.datetime.now()
    year = today.year
    start_of_year = datetime.datetime(year, 1, 1)
    next_year = datetime.datetime(year + 1, 1, 1)
    
    total_seconds_year = (next_year - start_of_year).total_seconds()
    elapsed_seconds = (today - start_of_year).total_seconds()
    percent = (elapsed_seconds / total_seconds_year) * 100
    days_left = (next_year - today).days

    # On prépare le bloc de texte SANS les balises à l'intérieur
    message = f"### 🗓️ {year} Year Progress\n{generate_progress_bar(percent)}\n\n⏳ **{days_left}** days left until {year + 1}!"

    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return

    # LA CORRECTION EST ICI :
    # On cherche ce qui est entre START et END et on remplace uniquement le milieu
    pattern = r"().*?()"
    replacement = f"\\1\n\n{message}\n\n\\2"
    
    # re.DOTALL est crucial pour que le "." capture aussi les retours à la ligne
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_year_progress()