from pathlib import Path

folder_path = Path(r"D:\YourFolder")

files = [
    file_path.name
    for file_path in folder_path.iterdir()
    if file_path.is_file()
]

print(files)