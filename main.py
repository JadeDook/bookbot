from stats import count_words, get_num_characters, sort_chars

def get_book_text(filepath) -> str:
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    character_count = get_num_characters(book_text)
    sort_characters = sort_chars(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sort_characters:
        letter = char["char"]
        num = char["num"]
        if letter.isalpha():
            print(f"{letter}: {num}")
    print("============= END ===============")

main()
