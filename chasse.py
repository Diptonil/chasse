from sys import exit

from exceptions import (
    argument_exceptions, 
    InvalidDirectoryPathException, 
    InvalidFilePathException,
    NoSpecifiedParentsException, 
    ParentAsDirectoryException, 
    ParentFilesNotFoundException,
    ParentPathNotSpecifiedException,
    ResultantFileNameNotSpecifiedException,
    MultiLineCommentBeforeParentDeclarationException,
    ChasseException
)
from utils.documents import ChildDocument
from utils.logs import logger
from utils.parsers import Parser


def main() -> None:
    """Client code logic."""

    parser = Parser()
    source_name = parser.get_source_name()
    destination_path = parser.get_destination_path()
    is_log_required = parser.get_log_requirement()
    logger.initialize_logger(is_log_required)

    try:
        resultant_file_name = parser.get_resultant_file_name()
        parent_path = parser.get_parent_path()
    except ChasseException as exception:
        if isinstance(exception, ParentPathNotSpecifiedException):
            logger.error("ERROR: There is no mention of the parent file path with the option -p or --parent-path.")
        elif isinstance(exception, ResultantFileNameNotSpecifiedException):
            logger.error("ERROR: There is no mention of the resultant file name with the option -n or --name.")
        exit(1)

    try:
        argument_exceptions(source_name, destination_path)
        if resultant_file_name != source_name.replace(".chasse", ""):
            child_document = ChildDocument(source_name, resultant_file_name)
        else:
            child_document = ChildDocument(source_name)
        child_document.convert(parent_path, destination_path)
    except FileNotFoundError as exception:
        logger.error("ERROR: " + str(exception))
    except InvalidDirectoryPathException:
        logger.error("ERROR: Path to the resultant directory needed, received a file.")
    except InvalidFilePathException:
        logger.error("ERROR: Path to the source file needed, received a directory.")
    except NoSpecifiedParentsException:
        logger.error("ERROR: The child Chasse files seem to have no specified parents. Check if all the parents have been declared starting from the 1st line, without any line-breaks.")
    except ParentAsDirectoryException:
        logger.error("ERROR: The specified parent declaration(s) in the child appear to be directories instead of files. Declare the used parent file instead of a directory.")
    except ParentFilesNotFoundException:
        logger.error("ERROR: There seem to be no parent Chasse files in the specified directory. Customise parent file paths using the `-p` flag (check help).")
    except MultiLineCommentBeforeParentDeclarationException:
        logger.error("ERROR: Multi-line HTML comments are not allowed before parent declarations. Restrict comments to a single line.")


if __name__ == "__main__":
    main()
