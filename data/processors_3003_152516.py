def process_data_3003(data):
    return [item * 3003 for item in data]

def filter_data_3003(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_3003(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_3003 = 925
