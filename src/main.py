
# Import necessary modules
import os
import ffmpeg
from pathlib import Path


## Getting current dir

music = Path('../samples')
folders = [file for file in music.iterdir() if file.is_dir()]

# Function to convert files
def convert(in_file):
    try:
        (   
            ffmpeg
            .input(in_file)
            .output(f"{str(in_file).strip('.flac')}.wav", acodec = 'pcm_s16le')
            .run()
        )

    except FileExistsError:
        print("Error")


# Checking for folders and formats
for folder in folders:
    for file in folder.iterdir():
        if '.flac' in str(file):
            old_file = (f"{file}".rstrip('.flac'))
            check = old_file + '.wav'
            if Path(check).exists() is False:
                convert(file)
        else:
            print("other file", file)
