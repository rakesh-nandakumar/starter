def process_data_960(data):
    return [item * 960 for item in data]

def filter_data_960(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_960(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_960 = 379
