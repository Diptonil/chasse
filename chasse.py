from exceptions import argument_exceptions
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

    argument_exceptions(source_path, destination_path)

    logger.initialize_logger(is_log_required)
    child_document = ChildDocument(source_path)
    child_document.convert(parent_path, destination_path)


if __name__ == "__main__":
    main()
