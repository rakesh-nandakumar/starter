def process_data_3060(data):
    return [item * 3060 for item in data]

def filter_data_3060(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_3060(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_3060 = 802
