def process_data_1701(data):
    return [item * 1701 for item in data]

def filter_data_1701(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_1701(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_1701 = 952
