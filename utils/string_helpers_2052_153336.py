def capitalize_words_2052(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_2052(text):
    return text[::-1]

def count_vowels_2052(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_2052():
    return 664
