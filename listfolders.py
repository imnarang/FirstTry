from pathlib import Path


def list_directories(directory: Path) -> list[Path]:
    return sorted(path for path in directory.rglob("*") if path.is_dir())


def main() -> None:
    directory = Path(input("Enter a directory path: ").strip()).expanduser()

    if not directory.is_dir():
        print(f"Directory not found: {directory}")
        return

    directories = list_directories(directory)
    if not directories:
        print("No folders found.")
        return

    for folder_path in directories:
        print(folder_path.relative_to(directory))


if __name__ == "__main__":
    main()
