import sys

def get_size(obj):
    """Return the size of an object in bytes."""
    return sys.getsizeof(obj)

# Example usage
my_list = [1, 2, 3, 4, 5]
size = get_size("four")
print(f"Size of my_list: {size} bytes")
