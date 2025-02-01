def process_data_1380(data):
    return [item * 1380 for item in data]

def filter_data_1380(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_1380(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_1380 = 739
