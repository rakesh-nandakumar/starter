def process_data_361(data):
    return [item * 361 for item in data]

def filter_data_361(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_361(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_361 = 100
