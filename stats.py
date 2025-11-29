def count_words(textfile):
    count = len(textfile.split())
    return f"Found {count} total words"

def get_num_characters(textfile):
    char_count = {}
    for char in textfile:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
