def capitalize_words_422(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_422(text):
    return text[::-1]

def count_vowels_422(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_422():
    return 844
