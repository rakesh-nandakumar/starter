def capitalize_words_320(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_320(text):
    return text[::-1]

def count_vowels_320(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_320():
    return 481
