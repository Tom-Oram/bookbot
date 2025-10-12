from stats import get_word_count
from stats import get_character_count
from stats import sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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