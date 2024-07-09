def capitalize_words_3450(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_3450(text):
    return text[::-1]

def count_vowels_3450(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_3450():
    return 906
