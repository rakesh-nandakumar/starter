def process_data_2120(data):
    return [item * 2120 for item in data]

def filter_data_2120(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_2120(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_2120 = 423
