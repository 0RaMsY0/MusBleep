import os


def iter_file(file_path: str):
    """
        Iter thraugh a file and yield it
    """
    with open(file_path, "rb") as file_content:
        yield from file_content
