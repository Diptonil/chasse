import os


def general_helper(html_path):
    if not os.path.exists(html_path):
        os.mkdir(html_path)
    os.chdir(html_path)
