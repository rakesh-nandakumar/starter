def process_data_13(data):
    return [item * 13 for item in data]

def filter_data_13(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_13(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_13 = 279
