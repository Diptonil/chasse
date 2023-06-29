from argparse import ArgumentParser
import os

from exceptions import exceptions


class Parser:
    """Defines the parser that would operate on the child HTML document."""

    def __init__(self) -> None:
        self.parser = ArgumentParser(prog="Chasse", description="Convert Chasse files to HTML files.")
        self.add_parser_arguments()

    def __str__(self) -> str:
        return "The main argument parser."

    def add_parser_arguments(self) -> None:
        """Adds all required arguments to the parser."""

        self.parser.add_argument("sourcepath", type=str, help="Enter the file path of the Chasse file to be converted into an HTML file.")
        self.parser.add_argument("destinationpath", type=str, help="Enter the directory wherein the HTML files will get stored.")
        self.parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0.0")

    def get_source_path(self) -> os.pa:
        """Returns the source file path."""

        args = vars(self.parser.parse_args())
        return args.get("sourcepath")
    
    def get_destination_path(self) -> str:
        """Returns the destination file path."""

        args = vars(self.parser.parse_args())
        return args.get("destinationpath")


class ResultantDocument:
    """Defines the final document that gets generated after processing."""

    def save(self):
        """Saves the file"""


class ChildDocument:
    """Defines the child document being parsed through."""

    def __init__(self, path: str) -> None:
        self.path = path

    def __str__(self) -> str:
        return "The source file that needs to be converted."
    
    def convert(self) -> ResultantDocument:
        """Returns the resultant document."""


def main():
    """Client code logic."""
    parser = Parser()
    source_path = parser.get_source_path()
    destination_path = parser.get_destination_path()

    exceptions(source_path, destination_path)

    child_document = ChildDocument(source_path)
    resultant_document = child_document.convert()
    resultant_document.save()


if __name__ == "__main__":
    main()