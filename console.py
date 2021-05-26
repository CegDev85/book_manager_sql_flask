import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Jack", "Jarvis")
author_repository.save(author1)

author2 = Author("Victor", "McDade")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("Dream Scheme", author1, "Thriller", 1995)
book_repository.save(book1)

book2 = Book("My Life in the Scheme", author2, "Horror", 1965)
book_repository.save(book2)

book3 = Book("Margret from doon the Road", author1, "Rom Com", 2000)
book_repository.save(book3)

book_repository.select_all()

pdb.set_trace()