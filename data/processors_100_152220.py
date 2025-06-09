def process_data_100(data):
    return [item * 100 for item in data]

def filter_data_100(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_100(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_100 = 87
