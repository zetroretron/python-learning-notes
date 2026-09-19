class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __repr__(self):
        return f"Book('{self.title}','{self.author}',{self.pages})"
    def __str__(self):
        return f"'{self.title}' by '{self.author}'"

    def __len__(self):
        return self.pages

class EBook(Book):
    def __init__(self,title,author,pages,file_size):
        super().__init__(title,author,pages)
        self.file_size=file_size


class Member():
    def __init__(self,name,member_id):
    self.name=name
    self.member_id=member_id
    self.borrowed_books= []

class Library():
    def __init__(self)
    self.books=[]

    def add_book(self,book):
        self.books.append(book)
    
    def remove_book(self,book):
        self.books.remove(book)
    
    def lend_book(Member,book):
        if book in self.books:
            Member.borrowed_books.append(book)
            remove_book(book)

        else:
            print("Book not available")


    def return_book(Member,book):
        if book in Member.borrowed_books:
            self.books.append(book)
            Member.borrowed_books.remove(book)
        else:
            print("no one took it dawg")
    
    





