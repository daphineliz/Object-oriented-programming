class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        
class Book(Author):
    def __init__(self, name, nationality, title, genre, availability):
        super().__init__(name, nationality)
        self.title = title
        self.genre = genre
        self.availability = availability
    #method to borrow
    def borrow_book(self):
        if self.availability == False:#if not self.availability:
            print(f"The book {self.title} has already been borrowed and is not available")
        
        else:
            self.availability = False #sets to false after the book has been borrowed
            print(f"You have borrowed the book {self.title}  by {self.name}")
            
#method to display book info
    def display_book_info(self):
        print(f"Title: {self.title} by {self.name}")
        print(f"Genre: {self.genre}")
        print(f"Availability: {self.availability}")
        print(f"Nationality: {self.nationality}")

book1 = Book("Anne", "Ugandan", "King's Curse", "Historical", True)
book2 = Book("James", "Kenyan", "Waffles", "Nursery rhyms", True)

book1.borrow_book()
book1.borrow_book()

book1.display_book_info()

