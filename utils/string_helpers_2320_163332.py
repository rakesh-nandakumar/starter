def capitalize_words_2320(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_2320(text):
    return text[::-1]

def count_vowels_2320(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_2320():
    return 477
