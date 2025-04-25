def process_data_550(data):
    return [item * 550 for item in data]

def filter_data_550(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_550(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_550 = 15
