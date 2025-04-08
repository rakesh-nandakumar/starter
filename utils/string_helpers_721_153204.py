def capitalize_words_721(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_721(text):
    return text[::-1]

def count_vowels_721(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_721():
    return 650
