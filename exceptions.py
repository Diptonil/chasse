import os


def argument_exceptions(source_path: str, destination_path: str):
    if os.path.isfile(destination_path):
        raise InvalidDirectoryPathException
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


class NoSpecifiedParentsException(ChasseException):
    """Thrown if the child document has no mentions of any parent document."""

    def __init__(self):            
        super().__init__(".")


class ParentAsDirectoryException(ChasseException):
    """Thrown if the child document bears mention of a parent document that is actualy a directory."""


class ParentFilesNotFoundException(ChasseException):
    """Thrown if the parent path does not have all files mentioned by a source file."""


class ComponentCountMismatchException(ChasseException):
    """Thrown if the count of the parsed components don't match the count of the required components."""
