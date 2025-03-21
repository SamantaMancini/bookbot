from stats import number_of_letters, dictionary_to_list

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        read_content = f.read()
        return read_content
    

def main():
    book_content = get_book_text("./books/frankenstein.txt")
    split_words = book_content.split()
    num_of_words = number_of_letters(split_words)
    letter_count = number_of_letters(book_content)

    print(f"\ttotal words: {len(num_of_words)}")

    allchar = dictionary_to_list(letter_count)

    for ele in allchar:
        print(f"\tLetter {ele["char"]} is used {ele["freq"]} times.")

main()