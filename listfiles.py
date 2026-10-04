from pathlib import Path


def list_files(directory: Path) -> list[Path]:
    return sorted(path for path in directory.rglob("*") if path.is_file())


def main() -> None:
    directory = Path(input("Enter a directory path: ").strip()).expanduser()

    if not directory.is_dir():
        print(f"Directory not found: {directory}")
        return

    files = list_files(directory)
    if not files:
        print("No files found.")
        return

    for file_path in files:
        print(file_path.relative_to(directory))


if __name__ == "__main__":
    main()