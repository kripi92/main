# class Stock:
#     def __init__(self, ticker, price, company):
#         self.ticker = ticker
#         self.price = price
#         self.company = company

#     def get_description(self):
#         return f'Stock: {self.ticker} is the ticker for {self.company} and the price is {self.price}'
# # Example usage
# msft = Stock("MSFT", 342.0, "Microsoft Corp")
# goog = Stock("GOOG", 135.0, "Google Inc")
# meta = Stock("META", 275.0, "Meta Platforms Inc")
# amzn = Stock("AMZN", 135.0, "Amazon Inc")

# print(msft.get_description())
# print(goog.get_description())
# print(meta.get_description())
# print(amzn.get_description())

class Product:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f'Product: {self.title}, ${self.author}'

class Periodical(Product):
    def __init__(self, title, author, price, period):
        super().__init__(title, author)
        self.price = price
        self.period = period


class Book(Product):
    def __init__(self, title, author, year, price):
        super().__init__(title, author)
        self.year = year
        self.price = price
    def __str__(self):
        return f'Book: {self.title} by {self.author}, {self.year}, ${self.price}'
class Ebook(Product):
    def __init__(self, title, author, year, price):
        super().__init__(title, author)
        self.year = year
        self.price = price
    def __str__(self):
        return f'Ebook: {self.title} by {self.author}, {self.year}, ${self.price}'
class Magazine(Periodical):
    def __init__(self, title, author, price, period):
        super().__init__(title, author, price,period)
        

    def __str__(self):
        return f'Magazine: {self.title} by {self.author}, {self.price}, ${self.period}'
class Newspaper(Periodical):
    def __init__(self, title, author, price, period):
        super().__init__(title, author, price,period)
    def __str__(self):
        return f'Newspaper: {self.title} by {self.author}, {self.price}, ${self.period}'


b1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951, 10.0)
eb1 = Ebook("The Catcher in the Rye", "J.D. Salinger", 1951, 5.0)
m1 = Magazine("Time", "Time Inc", 5.0, "Weekly")   
n1 = Newspaper("NY Times", "NY Times Inc", 2.0, "Daily")


print(b1)
print(eb1)
print(m1)
print(n1)

# print(b1.get_description())