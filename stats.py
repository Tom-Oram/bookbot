def get_word_count(text):
    split_text = text.split()
    return len(split_text)

def get_character_count(text):
    normalised = text.lower()
    dictionary = {}
    for character in normalised:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary