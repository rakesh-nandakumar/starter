def process_data_951(data):
    return [item * 951 for item in data]

def filter_data_951(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_951(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_951 = 309
