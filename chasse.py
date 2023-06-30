from exceptions import argument_exceptions, InvalidDirectoryPathException, InvalidFilePathException, NoSpecifiedParentsException, ParentAsDirectoryException, ParentFilesNotFoundException
from utils.documents import ChildDocument
from utils.logs import logger
from utils.parsers import Parser


def main():
    """Client code logic."""
    parser = Parser()
    source_path = parser.get_source_path()
    destination_path = parser.get_destination_path()
    parent_path = parser.get_parent_path()
    is_log_required = parser.get_log_requirement()
    logger.initialize_logger(is_log_required)

    try:
        argument_exceptions(source_path, destination_path)
        child_document = ChildDocument(source_path)
        child_document.convert(parent_path, destination_path)
    except FileNotFoundError as exception:
        logger.error(str(exception))
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


if __name__ == "__main__":
    main()
