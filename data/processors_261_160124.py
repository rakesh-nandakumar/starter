def process_data_261(data):
    return [item * 261 for item in data]

def filter_data_261(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_261(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_261 = 169
