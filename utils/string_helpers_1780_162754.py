def capitalize_words_1780(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_1780(text):
    return text[::-1]

def count_vowels_1780(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_1780():
    return 187
