
def text_len(text):
    return len(text)

def character_count(text):
    character_dic = {}
    for chracter in text:
        lower_char = chracter.lower()
        if lower_char.isalpha():
            if lower_char in character_dic:
                character_dic[lower_char] += 1
            else:
                character_dic[lower_char] = 1
    return character_dic
def sort_on(d):
   return d['num']

def sort_dic(dict):
    sorted_list = []
    for character in dict:
        sorted_list.append({"char": character, "num": dict[character]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    words = file_content.split()
    character_dictionary = character_count(file_content)
    sorted_list = sort_dic(character_dictionary)

    print(f"--- Beegin report of books/frankenstein.txt ---")
    print(f"{text_len(words)} words found in the document \n")
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times \n")
    print("--- End report ---")
main()
