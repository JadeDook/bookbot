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

def sort_on(items):
    return items["num"]

def sort_chars(chars):
    characters = []
    for i in chars:
        characters += [{"char":i,"num":chars[i]}]
    characters.sort(key=sort_on, reverse=True)
    return characters
