def process_data_3540(data):
    return [item * 3540 for item in data]

def filter_data_3540(data, threshold):
    return [x for x in data if x > threshold]

def sort_data_3540(data):
    return sorted(data, reverse=True)

MAGIC_NUMBER_3540 = 410
