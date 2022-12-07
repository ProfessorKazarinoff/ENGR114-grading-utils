# rename-file.py
"""
A simple Python script to copy and rename a files exported by the D2L LMS
"""

from pathlib import Path

src_str = "test"
src = Path(src_str)

dest_filename_str = src.stem.split(" - ")[1].split("-")[0] + "-" +  src.stem.split(" - ")[1].split("-")[2] + src.suffix
dest = Path(src.parent, dest_filename_str)

with open(dest, "w"):
    dest.write_text(src.read_text())
