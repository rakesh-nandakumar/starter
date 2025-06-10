def process_data_91(data):
    return [item * 91 for item in data]

def filter_data_91(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_91(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_91 = 386
