def remove_duplicates(lst):
    """Remove duplicates while preserving order"""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def chunk_list(lst, size):
    """Split list into chunks of specified size"""
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def flatten_list(nested_list):
    """Flatten nested list"""
    return [item for sublist in nested_list for item in sublist]
