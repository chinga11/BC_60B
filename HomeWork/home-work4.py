class Book:
    book3 = "Python", "Гвидо", 200
    def __init__(self, title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return f'{self.title} {self.author} {self.pages} '

    def __len__(self):
        return f'{self.pages} стр'
    def __add__(self, other):
        return f"Вместе {book1.pages + book2.pages} страниц"
    def __eq__ (self, other):
        if book1.pages == book2.pages:
            return True
        else:
            return False

    @classmethod
    def from_string (cls):
            return cls.book3

    @staticmethod
    def s_thick(pages, comparison):
        if pages > comparison:
            return True
        else:
            return False

class Mylist:
    def __init__(self,value):
        self.value = value


    def __getitem__(self, item):
        return self.value[item]
mylist = Mylist(["введение",1,2,3,4,5])

book1 = Book('1984', 'Дж. Оруелл', 328)
book2 = Book("Гарри Поттер"," Дж. Роулинг", 400)
print(book1.__str__())
print(book1.__len__())
print(book1.__add__(book2))
print(book1.__eq__(book2))
print(f'Глава {mylist [5]}, произведение "{book1.title}"')
print(Book.s_thick(book1.pages, 500))
print(Book.s_thick(book2.pages, 300))