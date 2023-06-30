from argparse import ArgumentParser, SUPPRESS
import os

from exceptions import NoSpecifiedParentsException, ParentAsDirectoryException, ParentFilesNotFoundException, ComponentCountMismatchException
from utils.logs import logger


class Parser:
    """Defines the parser that would operate on the child HTML document."""

    def __init__(self) -> None:
        self.parser = ArgumentParser(prog="Chasse", description="Convert child HTML files using components to HTML files.", add_help=False)
        self.add_parser_arguments()
        self.args = vars(self.parser.parse_args())


    def __str__(self) -> str:
        return "The main argument parser."

    def add_parser_arguments(self) -> None:
        """Adds all required arguments to the parser."""

        positional_arguments_group = self.parser.add_argument_group('POSITIONAL ARGUMENTS')
        positional_arguments_group.add_argument("source-file", type=str, help="The file path of the Chasse file to be converted into an HTML file.")
        positional_arguments_group.add_argument("destination-path", type=str, help="The directory wherein the HTML files will get stored.")
        options_group = self.parser.add_argument_group('OPTIONS')
        options_group.add_argument("-h", "--help", action="help", help="To show this help message.")
        options_group.add_argument("-v", "--version", action="version", version="%(prog)s 1.0.0", help="To show software's version number.")
        options_group.add_argument("-l", "--logs", action="store_true", help="To enable display of low-level logs (DEFAULT: False).")
        options_group.add_argument("-p", "--parent-path", action="store_true", help="To specify the path to the parent HTML files (DEFAULT: Child source path).")
    
    def get_source_path(self) -> str:
        """Returns the source file path."""

        return self.args.get("source-file")
    
    def get_destination_path(self) -> str:
        """Returns the destination file path."""

        return self.args.get("destination-path")
    
    def get_parent_path(self) -> str:
        """Returns the path to the parent files."""

        parent_path = self.args.get("parent-path")
        if parent_path is None:
            parent_path = os.path.dirname(self.get_source_path())
        return parent_path
    
    def get_log_requirement(self) -> bool:
        """Returns if low-level logs are required."""

        args, _ = self.parser.parse_known_args()
        return args.logs
    

def get_supposed_parent_file_names(source_path: str) -> list:
    """Returns all the parent file paths."""

    parent_files = list()
    has_no_parents = True
    with open(source_path, "r") as file:
        for line in file:
            line = line.strip()
            if line[-3:] != "!!>":
                break
            parent_files.append(line[1:-3] + '.chasse.html')
            has_no_parents = False
    if has_no_parents:
        raise NoSpecifiedParentsException
    if logger.is_log_required():
        logger.info(f"INFO: {len(parent_files)} parent file references found in `{source_path}`.")
    return parent_files


def check_supposed_parent_file_paths(parent_files: list, parent_path: str) -> None:
    """Checks received filenames against the files already present in the specified parent path."""

    resultant_parent_files = list()

    for file in os.listdir(parent_path):
        if os.path.isdir(file) and file in parent_files:
            raise ParentAsDirectoryException
        if file in parent_files:
            resultant_parent_files.append(file)
    if set(resultant_parent_files) != set(parent_files):
        raise ParentFilesNotFoundException
    if logger.is_log_required():
        logger.info("All parent file references intact.")
        

def get_requested_component_names(source_path: str) -> list:
    """Returns the requested component names."""

    requested_component_names = list()
    with open(source_path, "r") as file:
        for line in file:
            line = line.strip()
            if len(line) > 6 and line[-5:] == "!! />" and line[0] == "<" and line[1].isupper():
                requested_component_names.append(line[1:-5])
    if logger.is_log_required():
        logger.info(f"{len(requested_component_names)} components requested by the child file.")
    return requested_component_names


def get_components(requested_component_names: list, parent_file_names: list, parent_path: str) -> dict:
    """Returns the components from the parent files."""

    components = dict()
    component = list()
    active_component = False
    active_component_name = ""
    for file_name in parent_file_names:
        with open(os.path.join(parent_path, file_name), "r") as file:
            for line in file:
                output_line = line
                line = line.strip()
                if len(line) > 4 and line[-3:] == "!!>" and line[0] == "<" and line[1].isupper() and not active_component:
                    active_component_name = line[1:-3]
                    if active_component_name in requested_component_names:
                        active_component = True
                        continue
                if len(line) > 4 and line[-3:] == "!!>" and line[0] == "<" and line[2].isupper() and line[1] == "/" and active_component:
                    components[active_component_name] = component
                    component = list()
                    active_component = False
                if active_component:
                    component.append(output_line)
    if logger.is_log_required():
        logger.info(f"{len(components)} matching components found in the parent files.")
    return components


def check_component_retrieval(requested_component_names: list, components: dict) -> None:
    """Checks if all the components requested by the child document was succesfully retrieved."""

    if len(requested_component_names) != len(components):
        raise ComponentCountMismatchException
    