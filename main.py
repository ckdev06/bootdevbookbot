import os
import sys
from stats import get_num_words, get_char_dict, sort_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def main():
    book_text = get_book_text(sys.argv[1])
    
    print("============ BOOKBOT ============")
    
    print(f"Analyzing book found at {sys.argv[1]}...")
    
    print("----------- Word Count ----------")
    
    print(f"Found {get_num_words(book_text)} total words")

    print(sys.argv)
    
    #print(get_char_dict(book_text))

    char_counts = get_char_dict(book_text)

    sorted_chars = sort_dict(char_counts)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    
    


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content


    

    
   # print(get_book_text("books/frankenstein.txt"))



main()