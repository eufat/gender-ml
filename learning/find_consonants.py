def count_vowels(word):
    vowels = "aeiou"
    ch = word.lower()
    return sum(letter in vowels for letter in ch)

def count_consonants(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    ch = word.lower()
    return sum(letter in consonants for letter in ch)
