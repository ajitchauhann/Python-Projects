movies = {
    "action": ["John Wick", "Mad Max", "Extraction"],
    "comedy": ["Free Guy", "The Mask", "Jumanji"],
    "sci-fi": ["Interstellar", "Avatar", "The Matrix"]
}

genre = input("Enter genre: ").lower()

if genre in movies:
    print("Recommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("Genre not found.")



# AI Password Strength Checker:-

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1

    if score == 4:
        return "Strong Password"
    elif score >= 2:
        return "Medium Password"
    else:
        return "Weak Password"

pwd = input("Enter Password: ")
print(check_password(pwd)) 