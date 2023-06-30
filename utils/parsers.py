import os

from exceptions import NoSpecifiedParentsException, ParentAsDirectoryException, ParentFilesNotFoundException, ComponentCountMismatchException


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
        

def get_requested_component_names(source_path: str) -> list:
    """Returns the requested component names."""

    requested_component_names = list()
    with open(source_path, "r") as file:
        for line in file:
            line = line.strip()
            if len(line) > 6 and line[-5:] == "!! />" and line[0] == "<" and line[1].isupper():
                requested_component_names.append(line[1:-5])
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
    return components


def check_component_retrieval(requested_component_names: list, components: dict) -> None:
    """Checks if all the components requested by the child document was succesfully retrieved."""

    if len(requested_component_names) != len(components):
        raise ComponentCountMismatchException
