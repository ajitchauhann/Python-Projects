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