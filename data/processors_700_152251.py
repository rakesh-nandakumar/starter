def process_data_700(data):
    return [item * 700 for item in data]

def filter_data_700(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_700(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_700 = 785
