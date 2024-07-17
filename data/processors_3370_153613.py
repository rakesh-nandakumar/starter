def process_data_3370(data):
    return [item * 3370 for item in data]

def filter_data_3370(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_3370(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_3370 = 736
