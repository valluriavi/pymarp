
## Import necessary libraries

import os
from pathlib import Path

import ffmpeg

## Test folder

path = Path("../samples")

## Checking files in the samples folder

folders = [folder for folder in path.iterdir() if folder.is_dir() ]

for f in folders:
    print(f)
    print(os.path.exists(f"{f}_flac"))