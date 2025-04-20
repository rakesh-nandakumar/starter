def process_data_600(data):
    return [item * 600 for item in data]

def filter_data_600(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_600(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_600 = 595
