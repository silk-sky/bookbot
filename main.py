import sys
from stats import get_word_count
from stats import get_char_count
from stats import chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]


    text = get_book_text(book_path)
    print(text)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    character_count = get_char_count(text)
    print(character_count)
    chars_sorted_list = chars_dict_to_sorted_list(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ---")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as book:
        return book.read()



main()