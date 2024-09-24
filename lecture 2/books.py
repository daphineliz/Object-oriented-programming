#Example 1: library system
class Book:
    def __init__(self, title, author, pages, genre, volume):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre 
        self.volume = volume
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(f"{self.title} has been deleted")
        
        #method to get chapter
    def get_chapter(self, chapter):
        return f"{self.title} - Chapter {chapter}"
            
        #method to get author
    def get_author(self):
        return f"{self.title} is written by {self.author} and has{self.pages}"
    
    #method to show all the book"s info
    def show_info(self):
        return f"{self.title} by {self.author}, {self.pages} pages, {self.genre}, Volume {self.volume}"
    
    # create a book object of titl: The Moon also sets
book1 = Book("The Moon also sets", "John Doe", 300, "Self-Written", 1)
    
book2 = Book("The Art of racing in the rain", "Garth Sten", 400,"Fiction", 2 )
    
book3 = Book("King's Curse", "Daphineliz", 200, "historical", 2)