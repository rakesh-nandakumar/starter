def process_data_320(data):
    return [item * 320 for item in data]

def filter_data_320(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_320(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_320 = 371
