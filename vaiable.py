import json
class Book:
    def __init__(self,title, author, available, isbn):
        self.title = title
        self.author = author
        self.available = available
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Available: {self.available}, ISBN: {self.isbn}"    
    

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.available}, {self.isbn})"
    
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Available: {self.available}, ISBN: {self.isbn}"
    
    def mark_borrowed(self):
        if self.available:
            self.available = False
    
    def mark_returned(self):
        if not self.available:
            self.available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member Name: {self.name}, Member ID: {self.member_id}"
    
    def __repr__(self):
        return f"Member({self.name}, {self.member_id})"
    
    def borrow_book(self, book):
        if book.available:
            book.mark_borrowed()
            self.borrowed_books.append(book.title)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_returned()
            self.borrowed_books.remove(book.title)

    def display_borrowed_books(self):
        return [str(book) for book in self.borrowed_books]
    


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        return [str(book) for book in self.books]

    def display_members(self):
        return [str(member) for member in self.members]
    
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def list_available_books(self):
        return [str(book) for book in self.books if book.available]
    
    def borrow_book(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = self.find_book_by_title(book_title)
        if member and book and book.available:
            member.borrow_book(book)
            return f"{member.name} borrowed {book.title}."
        return "Borrowing failed. Either the book is not available or the member does not exist."
    
    def return_book(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = self.find_book_by_title(book_title)
        if member and book and book not in member.borrowed_books:
            return "Return failed. The book was not borrowed by this member."
        if book in member.borrowed_books:
            member.return_book(book)
            return f"{member.name} returned {book.title}."
        return "Return failed. The book was not borrowed by this member."


# Example usage
if __name__ == "__main__":
    library = Library()
    def operation():
        print("Library Management System")
        print("-----------------------------------------------------")  
        
        print("1. Add Book")
        print("2. Add Member")
        print("3. Display Books")
        print("4. Display Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        print("-----------------------------------------------------")
        print("Choose an operation:")
    
    
    
    def add_book():
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        available = input("Is the book available? (yes/no): ").lower() == 'yes'
        isbn = input("Enter book ISBN: ")
        book = Book(title, author, available, isbn)
        library.add_book(book)
        print(f"Book '{title}' added successfully.")

    def add_member():
        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")
        member = Member(name, member_id)
        library.add_member(member)
        print(f"Member '{name}' added successfully.")

    def display_books():
        print("Books in the library:")
        for book in library.display_books():
            print(book)

    def display_members():
        print("Members of the library:")
        for member in library.display_members():
            print(member)

    def borrow_book():
        member_id = input("Enter member ID: ")
        book_title = input("Enter book title to borrow: ")
        result = library.borrow_book(member_id, book_title)
        print(result)


    def return_book():

        member_id = input("Enter member ID: ")
        book_title = input("Enter book title to return: ")
        result = library.return_book(member_id, book_title)
        print(result)

    def store_data():
        with open('library_data.json', 'w') as file:
            data = {
                "books": [book.__dict__ for book in library.books],
                "members": [member.__dict__ for member in library.members]
            }
            json.dump(data, file, indent=4) 
    def load_data():    
        try:
            with open('library_data.json', 'r') as file:
                data = json.load(file)
                for book_data in data.get("books", []):
                    book = Book(**book_data)
                    library.add_book(book)
                for member_data in data.get("members", []):
                    member = Member(**member_data)
                    library.add_member(member)
        except FileNotFoundError:
            print("No previous data found. Starting fresh.")
    
    while True:
        operation()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            add_member()
        elif choice == '3':
            display_books()
        elif choice == '4':
            display_members()
        elif choice == '5':
            borrow_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            store_data()
            print("Exiting the system. Data saved.")
            break
        else:
            print("Invalid choice. Please try again.")
    
    
    load_data()