class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        # Returns a list of contracts related to this book
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        # Retrieves a list of authors related to this book using contracts
        return [contract.author for contract in self.contracts()]


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        # Returns a list of contracts related to this author
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        # Retrieves a list of books related to this author using contracts
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Validates inputs and creates a new contract with this author
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("royalties must be a non-negative integer")

        # Create contract and add it to author's contract list
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        # Calculate total royalties from all related contracts
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        # Validates contract data and initializes attributes
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("royalties must be a non-negative integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        # Returns all contracts matching the specified date
        return [contract for contract in cls.all_contracts if contract.date == date]

    # Adding an equality method to allow direct comparison of contract instances in assertions
    def __eq__(self, other):
        if isinstance(other, Contract):
            return (self.author == other.author and self.book == other.book and
                    self.date == other.date and self.royalties == other.royalties)
        return False
