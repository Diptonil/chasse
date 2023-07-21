from utils.parsers import (
    get_supposed_parent_file_names, 
    check_supposed_parent_file_paths, 
    get_requested_component_names, 
    get_components, 
    check_component_retrieval
)
from utils.writers import write_resultant_document


class ResultantDocument:
    """Defines the final document that gets generated after processing."""

    def __init__(self, parent_path: str, source_path: str, destination_path: str, resultant_file_name: str=None) -> None:
        self.parent_path = parent_path
        self.source_path = source_path
        self.destination_path = destination_path
        self.resultant_file_name = resultant_file_name
        self.save()

    def save(self):
        """Saves the resultant HTML file in the given directory."""
        parent_file_names: list = get_supposed_parent_file_names(self.source_path)
        check_supposed_parent_file_paths(parent_file_names, self.parent_path)
        requested_components: list = get_requested_component_names(self.source_path)
        components: dict = get_components(requested_components, parent_file_names, self.parent_path)
        check_component_retrieval(requested_components, components)
        write_resultant_document(self.source_path, self.destination_path, components, self.resultant_file_name)


class ChildDocument:
    """Defines the child document being parsed through."""

    def __init__(self, source_path: str, resultant_file_name :str=None) -> None:
        self.source_path = source_path
        self.resultant_file_name = resultant_file_name

    def __str__(self) -> str:
        return "The source file that needs to be converted."

    def convert(self, parent_path: str, destination_path: str) -> ResultantDocument:
        """Returns the resultant document."""

        return ResultantDocument(parent_path, self.source_path, destination_path, self.resultant_file_name)
