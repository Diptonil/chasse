import os


def write_resultant_document(source_path: str, destination_path: str, components: dict) -> None:
    """Writes data to the new resultant document in the specified location."""

    source_file_name = os.path.basename(source_path)
    source_file = open(source_path, "r")
    with open(os.path.join(destination_path, source_file_name), "w") as file:
        for line in source_file:
            output_line = line
            line = line.strip()
            if len(line) > 6 and line[-5:] == "!! />" and line[0] == "<" and line[1].isupper():
                component_name = line[1:-5]
                file.writelines(components[component_name])
                continue
            file.write(output_line)
    source_file.close()
