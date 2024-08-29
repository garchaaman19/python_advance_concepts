class Library:
    def __init__(self):
        self.is_book_taken = False
        self.available_books = [
            "MONK WHO SOLD HIS FERRARI",
            "ALCHEMIST",
            "PYSCHOLOGY OF MONEY",
        ]

    # when using decorator in a class outside func will only take func as argument
    # wrapper will take self
    def check_data_type(func):
        def wrap_func(self,*args, **kwargs):
            print(args)
            book=args[0]
            if not type(book)==str:
                return "Invalid"
            return func(*args,**kwargs)
        return wrap_func

    @check_data_type
    def check_book_available(func):
        def wrap_func(self, *args, **kwargs):
            book = args[0]
            if book.upper() in self.available_books:
                if (
                        self.is_book_taken == True
                ):
                    return "Book is available but is taken"
                else:
                    return "Book is Not available"
            return func(self, *args, **kwargs)
                # we return the function if everything is okay

        return wrap_func

    @check_book_available
    def borrow_book(self, requested_book):
        print("inside function")
        self.is_book_taken = False

    def return_book(self):
        pass


obj = Library()
requested_book = "ALCHEMIST"
print(obj.borrow_book(requested_book))
# User requests for book -how ?
# Librarian checks if book is available
# Also checks if book is taken by anyone
# If book available and not taken
# mark as not available and give to borrrower.
#
