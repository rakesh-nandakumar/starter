def process_data_400(data):
    return [item * 400 for item in data]

def filter_data_400(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_400(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_400 = 707
