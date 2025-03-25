# class Book:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     def __str__(self):
#         return f'{self.name} ({self.year})'
    

    
# book1 = Book('Harry Potter', 2000)
# print (book1)

# book1.name = 'Garry Potter'
# book1.year = 2001
# print(book1)

class Book:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def __str__(self):
        return f'{self.name} ({self.year})'


b1 = Book('Harry Potter', 2000)
b2 = Book('War and Peace', 2001)
print(b1)
print(b2)

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def __str__(self):
        return f"The Book {self.name} in the ({self.year})"

m1 = Movie('The Matrix', 1999)
m2 = Movie('Time', 1992)
print(m1)
print(m2)

print(type(b1))
print(type(m1))
# print(type(b1) == type(m1))
# print(type(b1) == type(b2))
# print(type(m1) == type(m2))

# print(isinstance(b1, Book))
# print(isinstance(m1, Book))
print(isinstance(m1, object))
