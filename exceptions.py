import os


def exceptions(source_path: str, destination_path: str):
    invalid_directory_path_exception(destination_path)
    invalid_file_path_exception(source_path)


def invalid_directory_path_exception(destination_path: str) -> None:
    if os.path.isfile(destination_path):
        raise InvalidDirectoryPathException
    

def invalid_file_path_exception(source_path: str) -> None:
    if os.path.isdir(source_path):
        raise InvalidFilePathException
    

class ChasseException(Exception):
    """Base exception of the application."""


class InvalidDirectoryPathException(ChasseException):
    """Thrown if the corresponding argument is a file instead of a directory."""

    def __init__(self):            
        super().__init__("Path to the resultant directory needed, received a file.")


class InvalidFilePathException(ChasseException):
    """Thrown if the corresponding argument is a directory instead of a file."""

    def __init__(self):            
        super().__init__("Path to the source file needed, received a directory.")
