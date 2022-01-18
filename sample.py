class Book:
    def __init__(self, name, publisher, isbn, selling_price=0):
        self.name = name
        self.publisher = publisher
        self.isbn = isbn
        self.__rating_stars = []

        if selling_price>0:
            self.__selling_price = selling_price
    def olchas():
        pass
    def old():
        pass
cl = Book('Olim', 'Tashkent', 34454023)
print(dir(cl))
