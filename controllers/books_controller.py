from flask import Flask, render_template, request, redirect, Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", authors = authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form["title"]
    genre = request.form["genre"]
    publisher = request.form["publisher"]
    author_id = request.form["author_id"]
    author = author_repository.select(author_id)
    book = Book(title, genre, publisher, author)
    book_repository.save(book)
    return redirect("/books")


# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/<id>")
def get_book(id):
    book = book_repository.select(id)
    return render_template("/books/find_book.html", book=book)

# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")
