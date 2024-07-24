def main():
    txt_location = "books/frankenstein.txt"
    text = read_text_from_file(txt_location)
    words = word_count(text)
    letter_count = lower_case_count(text.split())
    
    print_report(txt_location, words, letter_count)
    
def read_text_from_file(text):
    with open(text) as f:
        opened_text = f.read()
    return opened_text    

def word_count(text):
    words = text.split()
    return len(words)

def lower_case_count(word_list):
    letter_count = {}
    my_char = ord('a')
    
    while my_char <= ord('z'):
        letter_count[chr(my_char)] = 0
        my_char += 1
        
    for word in word_list:
        for letter in word.lower():
                if letter not in letter_count:
                    continue
                else:
                    letter_count[letter] += 1        
    
    return letter_count

def sort_on(dict):
    return dict[1]

def print_report(book_name, number_of_words, char_count_dict):
    print(f"--- Begin report of {book_name} ---")
    print(f"{number_of_words} words found in the document")
    
    dict_to_list = []
    for key, value in char_count_dict.items():
        dict_to_list.append([key, value])
    
    dict_to_list.sort(reverse=True, key=sort_on)
    for item in dict_to_list:
        print(f"The {item[0]} character was found {item[1]} times")
        
    print("--- End report ---")    
         

main()        