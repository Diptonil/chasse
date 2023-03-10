import argparse
import os

from argument_exceptions import exceptions

parser = argparse.ArgumentParser(description="Convert Chasse files to HTML files.")
parser.add_argument("filepath", type=str, help="Enter the file path of the Chasse file to be converted into an HTML file.")
parser.add_argument("htmlpath", type=str, help="Enter the directory wherein the HTML files will get stored.")
args = parser.parse_args()

file_path = args.filepath
html_path = args.htmlpath

exceptions(file_path, html_path)

if not os.path.exists(html_path):
    os.mkdir(html_path)

os.chdir(html_path)