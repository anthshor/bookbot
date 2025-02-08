def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    map = count_characters(file_contents)
    report(word_count, map)

def count_words(text):
    words = text.split() 
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    found = ""
    map = {}
    for char in lower_text:
        if char in found:
            map[char] += 1  
        else:
            found += char
            map[char] = 1 
    return map

def report(word_count, map):
    print("--- Begin report of books/frankenstein.txt -")
    print("")
    print(f"{word_count} words found in the document")
    print("")
    for item in map:
        if item >= 'a' and item <='z':
            print(f"The '{item}' character was found '{map[item]}' times")
    print("--- End report ---")



main()

