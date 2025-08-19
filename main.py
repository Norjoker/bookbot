import sys
from stats import count_words, char_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    #print(book)
    num_words = count_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_char = sort_dict(char_count(book))
    for l in num_char:
        if l[0].isalpha():
            print(f"{l[0]}: {l[1]}")
    print("============= END ===============")

if __name__=="__main__":
    main()
