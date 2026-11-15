
# Import necessary modules
import os
import ffmpeg
from pathlib import Path


# Functions in the program

def convert(in_file, format):
    try:
        (   
            ffmpeg
            .input(in_file)
            .output(f"{str(in_file).strip('.flac')}{format}")
            .run()
        )
    except FileExistsError:
        print("Error")

#, acodec = 'pcm_s16le') for lossless audio

def file_handler(folders, format):
    '''Handles the music files'''
    for folder in folders:
        for file in folder.iterdir():
            if '.flac' in str(file):
                old_file = (f"{file}".rstrip('.flac'))
                check = old_file + format
                if Path(check).exists() is False:
                    convert(file, format)
            else:
                print("File is already converted", file)

def input_handler():
    '''Handles the inputs'''
    try:
        music_folder = Path(input(str("Enter the directory for the music folder: ")))
        formats = {1: '.wav', 2: '.mp3', 3: '.aac'}
        format_option = int(input(f"Choose a format by typing the number (only integers): {formats}"))
        folders = [file for file in music_folder.iterdir() if file.is_dir()]

        file_handler(folders, formats[format_option] )

    except FileNotFoundError as e:
        print("There was an error in the program.")


def application():
    '''Main Overview application'''
    while True:
        print("Welcome to Music Converter V0.1")
        print("")
        input_handler()



application.run()