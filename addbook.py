





def add_book():
    bood_detail= input()
    author, title, publisher, publicationdate=bood_detail.split(',')
    book = {
    'author':author,
    'title':title,
    'publisher':publisher,
    'publicationdate':publicationdate
    

    }
    books.append(book)
    







def search_book(books, term):
    for book in books:
        
        if term in book.values():
            print(book)
            return True
    return False








           



   
if __name__ =="__main__":
    
    books=[]
    x=True
    while x==True:
        addorsearch=input("add books search or close ")
        if addorsearch =="add":
            add_book()
          
        elif addorsearch=="search":
            term=input("")
            search_book(books,term)
        else:
            x=False