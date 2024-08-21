from fastapi import *

app1 = FastAPI()

BOOKS = [
    {"Anand1": "hi", "Aditi1": 1000},
    {"Anand2": "say", "Aditi2": 100}

]

@app1.get("/books")
async def read_books():
    return BOOKS

@app1.get("/books/my_book")
async def read_books():
    return {"book_title": "my_fav_book"}

@app1.get("/books/{title}/")
async def read_books(title:str):
    for x in BOOKS:
        if x.get('Anand1').casefold() == title.casefold():
            return x

@app1.post("/books/creat_book")
async def add_book(creat_book=Body()):
    BOOKS.append(creat_book)

@app1.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('Anand1').casefold() == update_book.get('Anand1').casefold():
            BOOKS[i] = update_book
