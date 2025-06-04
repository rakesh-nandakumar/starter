def process_data_153(data):
    return [item * 153 for item in data]

def filter_data_153(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_153(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_153 = 888
