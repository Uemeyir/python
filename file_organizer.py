import os
from pathlib import Path
from sys import argv
from shutil import move


def get_dir(file):
    f = str(file)
    index_dot = f.rfind(".")
    exten = f[index_dot:]
    return dirs.get(exten, 'other')


dirs = {
    # Images
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.tiff': 'Images',

    # Videos
    '.mp4': 'Videos',
    '.mpv': 'Videos',
    '.avi': 'Videos',

    # Documents
    '.pdf': 'Documents',
    '.rtf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.odt': 'Documents',
    '.ppt': 'Documents',
    '.xls': 'Documents',
    '.zip': 'Documents',
    '.txt': 'Documents',

    # Program Files
    '.exe': 'Program Files',
    '.py': 'Program Files',
    '.html': 'Program Files',
    '.css': 'Program Files',
    '.cpp': 'Program Files',
    '.c': 'Program Files',
    '.js':  'Program Files',
    '.tar': 'Program Files',
    '.jar': 'Program Files',
}



if len(argv) != 2:
    print("Give one path to execute successfully")
    exit(1)

# The path to be organized
PATH = Path(argv[1])

# Iterate through the folder 
for file in PATH.iterdir():
    get_absolute_path = file.absolute()

    if get_absolute_path.is_file():
        # Get the directory name
        dir_name = get_dir(file)
        destination = PATH / dir_name

        # Make the destination folder if it doesn't exists
        if not destination.exists():
            destination.mkdir()
        
        move(str(get_absolute_path), str(destination))