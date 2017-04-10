
class SentenceSystem:
    """Libraries of managing words to sentences."""
    def count_vowels(self, word):
        vowels = "aeiou"
        ch = word.lower()
        return sum(letter in vowels for letter in ch)

    def count_consonants(self, word):
        consonants = "bcdfghjklmnpqrstvwxyz"
        ch = word.lower()
        return sum(letter in consonants for letter in ch)

    def reverse_sentence(self, alphabets):
        return alphabets[::-1]