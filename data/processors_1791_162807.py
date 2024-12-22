def process_data_1791(data):
    return [item * 1791 for item in data]

def filter_data_1791(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_1791(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_1791 = 533
