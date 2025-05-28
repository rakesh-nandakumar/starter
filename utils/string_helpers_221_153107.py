def capitalize_words_221(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_221(text):
    return text[::-1]

def count_vowels_221(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_221():
    return 458
