def process_data_2801(data):
    return [item * 2801 for item in data]

def filter_data_2801(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_2801(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_2801 = 136
