def main()->None:
    max_length = 0
    longest_words = []
    word = ""
    word_ending = [",", ".", " ", "\n"]
    
    file = open("elements.txt", "r")
    content = file.read()
    file.close()
    
    for char in content:
        if char in word_ending:
            if len(word) > max_length:
                longest_words.clear()
                max_length = len(word)
                longest_words.append(word)
            elif len(word) == max_length:
                longest_words.append(word)
            else:
                pass
            word = ""
        else:
            word = word + char
    print("The length of the longest word(s) is ", max_length)
    print("The words include: ")
    for word in longest_words:
        print(word)
main()