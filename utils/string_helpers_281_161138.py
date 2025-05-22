def capitalize_words_281(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_281(text):
    return text[::-1]

def count_vowels_281(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_281():
    return 736
