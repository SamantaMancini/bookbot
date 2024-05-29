def main():
   book_path = 'books/frankenstein.txt'
   text = book_text(book_path)
   words = get_num_words(text)
   lower_case = get_chars_dict(text)
   chars_sorted_list = chars_dict_to_sorted_list(lower_case)
   print(f"--- Begin report of {book_path} ---")
   print(f"{words} words found in the document")
   print()

   for item in chars_sorted_list:
      if not item["char"].isalpha():
            continue
      print(f"The '{item['char']}' character was found {item['num']} times")

   print("--- End report ---")
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

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

main()