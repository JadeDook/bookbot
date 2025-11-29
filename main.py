def get_book_text(filepath) -> str:
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(textfile):
    count = len(textfile.split())
    return f"Found {count} total words"

def main():
    book_text = get_book_text('books/frankenstein.txt')
    word_count = count_words(book_text)
    print(word_count)

main()
