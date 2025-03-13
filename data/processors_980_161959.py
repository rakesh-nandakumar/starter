def process_data_980(data):
    return [item * 980 for item in data]

def filter_data_980(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_980(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_980 = 655
