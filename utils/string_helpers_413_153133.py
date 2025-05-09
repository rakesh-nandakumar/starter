def capitalize_words_413(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_413(text):
    return text[::-1]

def count_vowels_413(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_413():
    return 353
