#06.16

class Ebook:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = 1
        self.is_open = False
        
    def open(self):
        self.is_open = True
        
    def close(self):
        self.is_open = False
        
    def next_page(self):
        if self.is_open==True:
            self.current_page = self.current_page + 1      
        
        if self.is_open==False:
            print("Książka jest zamknięta")
            
                       
    def show_status(self):
        print("Tytuł:", self.title)
        print("Autor:", self.author)
        print("Liczba stron:", self.number_of_pages)
        print("Nr bieżącej strony:", self.current_page)
        
      