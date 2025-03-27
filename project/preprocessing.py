from sys import exit
from pathlib import Path
if __name__ == "main":
    exit()

def load_and_save(path_to_data: Path | str, path_to_save: Path | str) -> tuple[list[Path], Path]:
    folder = Path(path_to_data).resolve()
    folder_to_save = Path(path_to_save).resolve()
    folder_to_save.mkdir(parents=True, exist_ok=True)

    paths = list(folder.rglob("*.wav"))

    for file_path in paths:
        relative_path = file_path.relative_to(folder)
        target_path = folder_to_save / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)

    return paths, folder_to_save


def process_files(files: list[Path], func,
                  path_to_data: Path | str,
                  path_to_save: Path | str, save_func) -> None:
    path_to_data = Path(path_to_data).resolve()
    path_to_save = Path(path_to_save).resolve()

    for file in files:
        processed_audio, sr = func(file)

        relative_path = file.relative_to(path_to_data)
        output_path = path_to_save / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        save_func(output_path, processed_audio, sr)
        print(f"Файл \"{file.name}\" успешно обработан и сохранён в {output_path}")