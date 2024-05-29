def main():
   book_path = 'books/frankenstein.txt'
   text = book_text(book_path)
   words = get_num_words(text)
   lower_case = get_chars_dict(text)
   print(lower_case)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def book_text(path):
     with open(path) as file:
        return file.read()

       


main()