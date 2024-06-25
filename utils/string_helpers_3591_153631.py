def capitalize_words_3591(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_3591(text):
    return text[::-1]

def count_vowels_3591(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_3591():
    return 926
