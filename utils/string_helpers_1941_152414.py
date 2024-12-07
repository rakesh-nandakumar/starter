def capitalize_words_1941(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_1941(text):
    return text[::-1]

def count_vowels_1941(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_1941():
    return 11
