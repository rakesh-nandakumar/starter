def process_data_2381(data):
    return [item * 2381 for item in data]

def filter_data_2381(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_2381(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_2381 = 888
