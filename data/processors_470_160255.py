def process_data_470(data):
    return [item * 470 for item in data]

def filter_data_470(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_470(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_470 = 501
