def capitalize_words_1401(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_1401(text):
    return text[::-1]

def count_vowels_1401(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_1401():
    return 201
