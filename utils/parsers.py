import os

from exceptions import NoSpecifiedParentsException, ParentAsDirectoryException, ParentFilesNotFoundError


def get_supposed_parent_file_names(source_path: str):
    """Returns all the parent file paths."""

    parent_files = list()
    has_no_parents = True
    with open(source_path, "r") as file:
        for line in file:
            line = line.strip()
            if line[-3:-1] != "!!":
                break
            parent_files.append(line[1:-3] + '.html')
            has_no_parents = False
    if has_no_parents:
        raise NoSpecifiedParentsException
    return parent_files


def check_supposed_parent_file_paths(parent_files: list, parent_path: str):
    """Checks received filenames against the files already present in the specified parent path."""

    resultant_parent_files = list()

    for file in os.listdir(parent_path):
        print(file)
        if os.path.isdir(file) and file in parent_files:
            print(os.path.isdir(file))
            raise ParentAsDirectoryException
        if file in parent_files:
            resultant_parent_files.append(file)
    print(resultant_parent_files)
    print(parent_files)
    if set(resultant_parent_files) != set(parent_files):
        raise ParentFilesNotFoundError
        