import argparse
import os

from argument_exceptions import exceptions
from src.general import general_helper


def main():
    parser = argparse.ArgumentParser(prog="Chasse", description="Convert Chasse files to HTML files.")
    parser.add_argument("filepath", type=str, help="Enter the file path of the Chasse file to be converted into an HTML file.")
    parser.add_argument("htmlpath", type=str, help="Enter the directory wherein the HTML files will get stored.")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")

    args = vars(parser.parse_args())
    file_path = args.get("filepath")
    html_path = args.get("htmlpath")

    exceptions(file_path, html_path)
    general_helper(html_path)


if __name__ == "__main__":
    main()