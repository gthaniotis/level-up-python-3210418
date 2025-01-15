import json

def save_dict(dictionary, file_path):
    """
    Save a dictionary to a file in JSON format.

    :param dictionary: The dictionary to save.
    :param file_path: The path to the output file.
    """
    with open(file_path, 'w') as file:
        json.dump(dictionary, file)

def load_dict(file_path):
    """
    Load a dictionary from a file in JSON format.

    :param file_path: The path to the input file.
    :return: The loaded dictionary.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

# Example usage:
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
file_path = '/workspaces/level-up-python-3210418/src/06 Save a Dictionary/my_dict.json'

# Save the dictionary to a file
save_dict(my_dict, file_path)

# Load the dictionary from the file
loaded_dict = load_dict(file_path)
print(loaded_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}