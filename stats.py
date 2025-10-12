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

def sorted_list(text):  
    sorted_list = [{"char": k, "num": v} for k, v in text.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(item):
    return item["num"]