def process_data_501(data):
    return [item * 501 for item in data]

def filter_data_501(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_501(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_501 = 151
