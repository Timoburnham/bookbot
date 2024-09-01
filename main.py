def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

        num_words = len(file_contents.split())
        print(num_words)
        
    char_freq = {}
    

    for i in file_contents:
        lowered = i.lower()
        if lowered.isalpha():
            if lowered in char_freq:
                char_freq[lowered] += 1
            else:
                char_freq[lowered] = 1
        

    print("Report of book, Frankenstein")
    print(f" There are {num_words} words in the book.")
    print(" ")
    for i in char_freq:
        print(f"The '{i}' character was found {char_freq[i]} times")
    print("--end report--")
main()