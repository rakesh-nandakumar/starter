def capitalize_words_61(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_61(text):
    return text[::-1]

def count_vowels_61(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_61():
    return 626
