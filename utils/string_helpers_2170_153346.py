def capitalize_words_2170(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_2170(text):
    return text[::-1]

def count_vowels_2170(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_2170():
    return 330
