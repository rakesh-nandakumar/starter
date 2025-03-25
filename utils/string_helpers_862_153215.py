def capitalize_words_862(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_862(text):
    return text[::-1]

def count_vowels_862(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_862():
    return 576
