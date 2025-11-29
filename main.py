from stats import count_words, get_num_characters

def get_book_text(filepath) -> str:
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text('books/frankenstein.txt')
    word_count = count_words(book_text)
    character_count = get_num_characters(book_text)
    print(word_count)
    print(character_count)

main()
