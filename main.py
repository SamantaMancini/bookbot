from stats import number_of_letters, dictionary_to_list, sort_on

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        read_content = f.read()
        return read_content
    

def main():
    path = "./books/frankenstein.txt"
    book_content = get_book_text(path)
    split_words = book_content.split()
    num_of_words = number_of_letters(split_words)
    letter_count = number_of_letters(book_content)

    print(f"------------- Report of {path} -------------")

    print(f"\ttotal words: {len(num_of_words)}")

    allchar = dictionary_to_list(letter_count)
    allchar.sort(reverse=True, key=sort_on)

    for ele in allchar:
        print(f"\tLetter {ele["char"]} is used {ele["freq"]} times.")

    print(f"------------ End of Report {path} ---------")

main()