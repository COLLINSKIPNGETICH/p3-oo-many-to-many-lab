# many_to_many.py

class Book:
    _all_books = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._all_books.append(self)

    @classmethod
    def all_books(cls):
        return cls._all_books

    def contracts(self):
        return self._contracts

    def authors(self):
        return list(set(contract.author for contract in self._contracts))


class Author:
    _all_authors = []

    def __init__(self, name):
        self.name = name
        self._all_contracts = []
        self._all_books = []
        self._all_authors.append(self)

    @classmethod
    def all_authors(cls):
        return cls._all_authors

    def contracts(self):
        return self._all_contracts

    def books(self):
        return self._all_books

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        contract = Contract(self, book, date, royalties)
        self._all_contracts.append(contract)
        self._all_books.append(book)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._all_contracts)


class Contract:
    _all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author")
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self._all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return sorted([contract for contract in cls._all_contracts if contract.date == date], key=lambda x: x.date)
