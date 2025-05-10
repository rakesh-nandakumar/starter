def process_data_402(data):
    return [item * 402 for item in data]

def filter_data_402(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_402(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_402 = 731
