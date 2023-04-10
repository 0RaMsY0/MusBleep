import string
import random

def random_id() -> str:
    """
        Generate a random id
    """
    chars = [letter for letter in str(string.ascii_letters+str(1234567890))]
    _id = ""


    while len(_id) <= 7:
        _id += random.choice(chars)

    return _id

