def process_data_870(data):
    return [item * 870 for item in data]

def filter_data_870(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_870(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_870 = 95
