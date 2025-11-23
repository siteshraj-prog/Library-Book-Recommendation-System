library = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction", "level": "Easy"},
    {"title": "Sherlock Holmes", "author": "Arthur Conan Doyle", "genre": "Mystery", "level": "Medium"},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "genre": "Science", "level": "Hard"},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "genre": "Finance", "level": "Easy"},
    {"title": "Deep Work", "author": "Cal Newport", "genre": "Productivity", "level": "Medium"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy", "level": "Easy"},
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-Help", "level": "Easy"},
]

def show_books():
    print("\nLibrary Books:\n")
    for b in library:
        print(b["title"], "|", b["author"], "|", b["genre"], "|", b["level"])

def recommend(g, lvl):
    print("\nRecommended Books:\n")
    f = False
    for b in library:
        if b["genre"].lower() == g.lower() and b["level"].lower() == lvl.lower():
            print(b["title"], "by", b["author"])
            f = True
    if not f:
        print("No match found")

def main():
    while True:
        print("\nLibrary Book Recommendation System")
        print("1. View all books")
        print("2. Get recommendations")
        print("3. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            show_books()
        elif ch == "2":
            print("Genres: Fiction, Mystery, Science, Finance, Productivity, Fantasy, Self-Help")
            g = input("Enter genre: ")
            lvl = input("Enter level (Easy/Medium/Hard): ")
            recommend(g, lvl)
        elif ch == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()