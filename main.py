#!/usr/bin/env python3

import sys
from stats import get_book_text, count_words, count_characters, sort_character_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_text = get_book_text(filepath)

    if not book_text:
        sys.exit(1)

    word_count = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_counts = count_characters(book_text)
    sorted_characters = sort_character_counts(char_counts)

    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    print("============ END ===============")

if __name__ == "__main__":
    main()