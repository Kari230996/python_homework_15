import os
import logging
from collections import namedtuple

FileEntry = namedtuple(
    'FileEntry', ['name', 'extention', 'is_directory', 'parent_directory'])


logging.basicConfig(filename='file_info.log',
                    level=logging.INFO, format='%(asctime)s - %(message)s')


def get_file_info(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for dir_name in dirs:
            parent_dir = os.path.basename(
                os.path.dirname(os.path.join(root, dir_name)))
            file_entry = FileEntry(dir_name, None, True, parent_dir)
            logging.info(f"Directory: {file_entry}")

        for file_name in files:
            file, ext = os.path.splitext(file_name)
            parent_dir = os.path.basename(root)
            file_entry = FileEntry(file, ext, False, parent_dir)
            logging.info(f"File: {file_entry}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Collect information about files and directories.")
    parser.add_argument("directory_path", type=str,
                        help="Path to the directory to analiyze")

    args = parser.parse_args()
    directory_path = args.directory_path

    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        get_file_info(directory_path)
