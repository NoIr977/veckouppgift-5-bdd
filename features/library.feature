Feature: Library

Scenario Outline: Find a book by name

Given a book with title <title> is in the library
When the user searches for the book by title <title>
Then the book with title <title> is found

Examples:
  | title        |
  | Harry Potter |


Scenario Outline: Find a book by author

Given a book with author <author> is in the library
When the user searches for the book by author <author>
Then the book with author <author> is found

Examples:
  | author         |
  | Sidney Sheldon |


Scenario Outline: Borrow a book from the library

Given the book <title> is in the library
When the user borrows the book <title>
Then the book <title> should be borrowed

Examples:
  |title                           |
  |Harry Potter: The Goblet of Fire|

Scenario Outline: Return the book to the library

Given the book <title> is borrowed
When the user returns the book <title> to the library
Then the book <title> should not be borrowed

Examples:
  |title                           |
  |Harry Potter: The Goblet of Fire|


Scenario Outline: Check if a book is borrowed

  Given the book <title> has status <status>
  When the user checks the status of the book <title>
  Then the status <status> should be shown

Examples:
  | title              | status       |
  | Harry Potter       | borrowed     |
  | Gone with the Wind | not borrowed |

