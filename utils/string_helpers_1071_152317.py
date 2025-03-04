def capitalize_words_1071(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_1071(text):
    return text[::-1]

def count_vowels_1071(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_1071():
    return 336
