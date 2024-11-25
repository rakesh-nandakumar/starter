def process_data_2060(data):
    return [item * 2060 for item in data]

def filter_data_2060(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_2060(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_2060 = 456
