vowels = ['a', 'e', 'i', 'o', 'u']

word = "Milliways"

for letter in word:    # takes each letter in the word
    if letter in vowels:   # and if it matches in the vowels list
        print (letter)     # display the letter
