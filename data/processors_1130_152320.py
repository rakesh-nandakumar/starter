def process_data_1130(data):
    return [item * 1130 for item in data]

def filter_data_1130(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_1130(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_1130 = 106
