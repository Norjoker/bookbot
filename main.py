def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def count_words(text):
    words = text.split()
    count = len(words)
    return count

def main():
    book = get_book_text("books/frankenstein.txt")
    #print(book)
    num_words = count_words(book)
    print(f"{num_words} words found in the document")

if __name__=="__main__":
    main()
