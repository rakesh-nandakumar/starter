def capitalize_words_3250(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_3250(text):
    return text[::-1]

def count_vowels_3250(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_3250():
    return 288
