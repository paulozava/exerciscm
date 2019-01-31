def calculate_total(books):
    books_price = {1:800, 2:760, 3:720, 4:640, 5:600}
    total = 0
    while books:
        removed = 0
        for book in range(1,6):
            if book in books:
                books.remove(book)
                removed +=1
        total += books_price[removed] * removed
    return total