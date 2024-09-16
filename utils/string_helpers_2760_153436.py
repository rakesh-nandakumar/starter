def capitalize_words_2760(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string_2760(text):
    return text[::-1]

def count_vowels_2760(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

def random_function_2760():
    return 721
