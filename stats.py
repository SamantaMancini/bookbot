def number_of_letters(text):
    letter_set = {}
    for c in text:
        key = c.lower()
        if key in letter_set:
            letter_set[key] += 1
            continue
        letter_set[key] = 1
    return letter_set

def dictionary_to_list(dictionary):
    list = []
    for key in dictionary.keys():
        if key.isalpha():
            list.append({"char":key, "freq":dictionary[key]})
    return list