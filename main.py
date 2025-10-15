from stats import get_word_count
from stats import get_character_count
from stats import sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def validate_args(expected_count):
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    validate_args(sys.argv)
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    word_count = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = get_character_count(book_text)
    sort = sorted_list(character_count)
    for dictionary in sort:
        ch = dictionary["char"]
        cnt = dictionary["num"]
        if ch.isalpha():
            print(f"{ch}: {cnt}")
    print("============= END ===============")

main()