# rename-file.py
"""
A simple Python script to rename a files exported by the D2L LMS
"""

from pathlib import Path

old_f_str = "/Users/peter.kazarinoff/Downloads/Lab 1 Download Dec 6, 2022 455 PM/545474-744367 - first.last-Sep 29, 2022 342 PM-lab1.ipynb"
old_f_path = Path(old_f_str)

new_f_str = "/Users/peter.kazarinoff/Downloads/Lab 1 Download Dec 6, 2022 455 PM/first.last-file1.ipynb"
new_f_path = old_f_path.with_name(new_f_str)

print(f"renamed: {str(old_f_path)} to: {str(new_f_path)}")
