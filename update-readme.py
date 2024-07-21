from datetime import datetime, timedelta

# Date de naissance
birth_date = datetime(2002, 8, 19)

# Date actuelle
today = datetime.now()

# Calculer la prochaine date d'anniversaire
current_year = today.year
next_birthday = datetime(current_year, birth_date.month, birth_date.day)

if today > next_birthday:
    next_birthday = datetime(current_year + 1, birth_date.month, birth_date.day)

# Calculer le nombre de jours restants
days_until_birthday = (next_birthday - today).days

# Calculer l'âge
age = today.year - birth_date.year
if today < datetime(today.year, birth_date.month, birth_date.day):
    age -= 1

# Préparer le message
if days_until_birthday == 0:
    message = f"Aujourd'hui j'ai {age} ans !!"
else:
    message = f"Dans {days_until_birthday} jours, j'aurai {age} ans !"

# Écrire le message dans le README
with open("README.md", "w") as f:
    f.write(f"# Bonjour !\n\n{message}\n")
