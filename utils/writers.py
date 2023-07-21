import os

from utils.logs import logger


def write_resultant_document(source_path: str, destination_path: str, components: dict, resultant_file_name: str = None) -> None:
    """Writes data to the new resultant document in the specified location."""

    if resultant_file_name is None:
        source_file_name = os.path.basename(source_path).replace(".chasse", "")
    else:
        source_file_name = os.path.basename(resultant_file_name)
    source_file = open(source_path, "r")
    with open(os.path.join(destination_path, source_file_name), "w") as file:
        for line in source_file:
            output_line = line
            spaces = len(line) - len(line.lstrip(" ")) - 4
            line = line.strip()
            if len(line) > 6 and line[-5:] == "!! />" and line[0] == "<" and line[1].isupper():
                component_name = line[1:-5]
                spaces = str(" " * spaces)
                lines = [spaces + line for line in components[component_name]]
                file.writelines(lines)
                continue
            file.write(output_line)
    source_file.close()
    logger.initialize_logger(True)
    if logger.is_log_required():
        logger.info(f"SUCCESS: Resultant file `{source_file_name}` has been generated in `{destination_path}`!")
