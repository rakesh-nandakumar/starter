def process_data_231(data):
    return [item * 231 for item in data]

def filter_data_231(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_231(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_231 = 241
