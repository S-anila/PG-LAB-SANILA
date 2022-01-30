classpublisher:
    def__init__(self,title,author):
        self.title=title
        self.author=author
    defdisplay(self):
        print("Title:",self.title)
        print("Author:",self.author)
classbook(publisher):
    def__init__(self,price,no_of_page):
        self.price=price
        self.no_of_page=no_of_page
    defdisplay(self):
        print("Price:",self.price)
        print("No. of Pages:",self.no_of_page)
classpython(book):
    def__init__(self,title,author,price,no_of_page):
        publisher.__init__(self,title,author)
        book.__init__(self,price,no_of_page)
    defdisplay(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
        print("No. of Pages:",self.no_of_page)
p=python("Python Programming","m mukundhan",2000,200)
p.display()
