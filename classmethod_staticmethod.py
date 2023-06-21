class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

        @classmethod
        def class_method(cls):
            print(f"called class_method of {cls}")

        @staticmethod
        def static_method():
            print("Called static_method")

ClassTest.class_method()

ClassTest.static_method()

test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

book = Book("Harry Potter", "hardcover", 1500)

book_1 = Book.hardcover("harry Potter", 1500)
light = Book.paperback("python 101", 600)

print(book)

