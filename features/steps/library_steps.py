from behave import given, when, then
from src.library import Book, Library

@given("a book with title {title} is in the library")
def step_book_with_title(context, title):
    context.library = Library()
    context.book = Book(title, "Unknown")
    context.library.add_book(context.book)


@when("the user searches for the book by title {title}")
def step_find_by_title(context, title):
    context.found_book = context.library.find_by_title(title)


@then("the book with title {title} is found")
def step_book_is_found(context, title):
    assert context.found_book.title == title


@given("a book with author {author} is in the library")
def step_book_with_author(context, author):
    context.library = Library()
    context.book = Book("Unknown", author)
    context.library.add_book(context.book)


@when("the user searches for the book by author {author}")
def step_find_by_author(context, author):
    context.found_book = context.library.find_by_author(author)


@then("the book with author {author} is found")
def step_book_by_author_is_found(context, author):
    assert context.found_book.author == author


@given("the book {title} is in the library")
def step_book_in_library(context, title):
    context.library = Library()
    context.book = Book(title, "Unknown")
    context.library.add_book(context.book)

@when("the user borrows the book {title}")
def step_borrow_book(context,title):
    context.library.borrow_book(title)

@then("the book {title} should be borrowed")
def step_book_should_be_borrowed(context, title):
    assert context.book.check_status() == True

@given("the book {title} is borrowed")
def step_book_is_borrowed(context,title):
    context.library = Library()
    context.book = Book(title, "Unknown")
    context.library.add_book(context.book)
    context.library.borrow_book(title)

@when("the user returns the book {title} to the library")
def step_return_book(context, title):
    context.library.return_book(title)

@then("the book {title} should not be borrowed")
def step_book_is_not_borrowed(context,title):
    assert context.book.check_status() == False

@given("the book {title} has status {status}")
def step_book_has_status(context, title, status):
    context.library = Library()
    context.book = Book(title, "Unknown")
    context.library.add_book(context.book)

    if status == "borrowed":
        context.book.borrow()

@when("the user checks the status of the book {title}")
def step_check_book_status(context, title):
    context.status = context.book.check_status()

@then("the status {status} should be shown")
def step_status_is_shown(context, status):
    if status == "borrowed":
        expected_status = True
    else:
        expected_status = False

    assert context.status == expected_status


