class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."
    
shelf = BookShelf(300)

print(shelf)

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Book {self.name}"
    
book = Book("LOTR")
book2 = Book("Sing 2")

shelf = BookShelf(book, book2)

print(shelf)