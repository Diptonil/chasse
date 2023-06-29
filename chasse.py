from argparse import ArgumentParser
import os

from exceptions import argument_exceptions
from utils.parsers import get_supposed_parent_file_names, check_supposed_parent_file_paths, get_requested_component_names, get_components, check_component_retrieval
from utils.writers import write_resultant_document


class Parser:
    """Defines the parser that would operate on the child HTML document."""

    def __init__(self) -> None:
        self.parser = ArgumentParser(prog="Chasse", description="Convert Chasse files to HTML files.")
        self.add_parser_arguments()

    def __str__(self) -> str:
        return "The main argument parser."

    def add_parser_arguments(self) -> None:
        """Adds all required arguments to the parser."""

        self.parser.add_argument("source", type=str, help="Enter the file path of the Chasse file to be converted into an HTML file.")
        self.parser.add_argument("destinationpath", type=str, help="Enter the directory wherein the HTML files will get stored.")
        self.parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0.0")
        self.parser.add_argument("-p", "--parent-path", help="To specify the path to the parent files. Defaults to the source path.")

    def get_source_path(self) -> str:
        """Returns the source file path."""

        args = vars(self.parser.parse_args())
        return args.get("source")
    
    def get_destination_path(self) -> str:
        """Returns the destination file path."""

        args = vars(self.parser.parse_args())
        return args.get("destinationpath")
    
    def get_parent_path(self) -> str:
        """Returns the path to the parent files."""

        args = vars(self.parser.parse_args())
        parent_path = args.get("parent-path")
        if parent_path is None:
            parent_path = os.path.dirname(self.get_source_path())
        return parent_path


class ResultantDocument:
    """Defines the final document that gets generated after processing."""

    def __init__(self, parent_path: str, source_path: str, destination_path: str) -> None:
        self.parent_path = parent_path
        self.source_path = source_path
        self.destination_path = destination_path
        self.save()

    def save(self):
        """Saves the file."""
        parent_file_names: list = get_supposed_parent_file_names(self.source_path)
        print(parent_file_names)
        check_supposed_parent_file_paths(parent_file_names, self.parent_path)
        requested_components: list = get_requested_component_names(self.source_path)
        print(requested_components)
        components: dict = get_components(requested_components, parent_file_names, self.parent_path)
        print(components)
        check_component_retrieval(requested_components, components)
        write_resultant_document(self.source_path, self.destination_path, components)


class ChildDocument:
    """Defines the child document being parsed through."""

    def __init__(self, source_path: str) -> None:
        self.source_path = source_path

    def __str__(self) -> str:
        return "The source file that needs to be converted."
    
    def convert(self, parent_path: str, destination_path: str) -> ResultantDocument:
        """Returns the resultant document."""

        return ResultantDocument(parent_path, self.source_path, destination_path)


def main():
    """Client code logic."""
    parser = Parser()
    source_path = parser.get_source_path()
    destination_path = parser.get_destination_path()
    parent_path = parser.get_parent_path()

    argument_exceptions(source_path, destination_path)

    child_document = ChildDocument(source_path)
    child_document.convert(parent_path, destination_path)


if __name__ == "__main__":
    main()