from stats import get_word_count
from stats import get_character_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    print(f"Found {word_count} total words")
    print(character_count)


main()