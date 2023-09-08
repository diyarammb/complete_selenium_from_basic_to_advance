class Book:
    count = 0
    def __init__(self,isbn, title, author, publisher, pages, price, copies):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.publisher=publisher
        self.pages=pages
        self.price=price
        self.copies=copies

        Book.count += 1

    def display(self):

        # print(i)
        print('isbn :',self.isbn,'Title :',self.title,'Author :',self.author,'Publisher :',self.publisher,'Pages :',self.pages,'Price :',self.price,'CBC :',self.copies)

b1=Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
b2=Book('957-4-36-547417-2', 'Learn python','Daya', 'CBC', 350, 300,100)
print('========================Book Details==============================')
b1.display()
print('========================Book Details==============================')
b2.display()
Book.count
