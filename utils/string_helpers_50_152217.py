def capitalize_words_50(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_50(text):
    return text[::-1]

def count_vowels_50(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_50():
    return 322
