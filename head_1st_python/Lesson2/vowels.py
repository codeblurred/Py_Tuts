vowels = ['a', 'e', 'i', 'o', 'u']

word = input("provide a word to search for vowels : ")


found = [] # starts with empty list

for letter in word:    # takes each letter in the word
    if letter in vowels:   # and if it matches in the vowels list
        if letter not in found:
            found.append(letter)


for vowel in found:
    print(vowel)
