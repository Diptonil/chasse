import os


def exceptions(file_path, html_path):
    file_path_exception(file_path)
    html_path_exception(html_path)
    

def file_path_exception(file_path):
    if file_path[-7:] != ".chasse":
        raise Exception("Unsuitable file. File must have .chasse as the extension.")
    

def html_path_exception(html_path):
    if os.path.isfile(html_path):
        raise Exception("Path to the resultant directory needed, not a file.")
