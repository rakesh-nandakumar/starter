def process_data_970(data):
    return [item * 970 for item in data]

def filter_data_970(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_970(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_970 = 164
