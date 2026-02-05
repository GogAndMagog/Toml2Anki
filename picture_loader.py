import shutil
import urllib.request
from encodings.punycode import selective_find
from pathlib import Path

PICTURES_SOURCE = r"https://zhukovsd.github.io"
PICTURES_DESTINATION = r"pictures"

class PictureHandler:

    pictures = []

    def __init__(self):
        self.pictures = []

    def download_picture(self, destination: str, path: str) -> str:
        data = (urllib.request
                .urlopen(PICTURES_SOURCE + path)
                .read())
        dir_path = Path(destination) / PICTURES_DESTINATION / path.lstrip('/')
        dir_path.parent.mkdir(parents=True, exist_ok=True)
        dir_path.write_bytes(data)

        self.pictures.append(str(dir_path))

        return str(dir_path)

    def delete_pictures_dir(self, destination: str):
        dir_path = Path(destination) / PICTURES_DESTINATION
        if dir_path.exists() and dir_path.is_dir():
            shutil.rmtree(dir_path)


def download_picture(destination: str, path: str) -> str:

    data = (urllib.request
            .urlopen(PICTURES_SOURCE + path)
            .read())
    dir_path = Path(destination) / PICTURES_DESTINATION / path.lstrip('/')
    dir_path.parent.mkdir(parents=True, exist_ok=True)
    dir_path.write_bytes(data)

    return str(dir_path)

def delete_pictures_dir(destination: str):
    dir_path = Path(destination) / PICTURES_DESTINATION
    if dir_path.exists() and dir_path.is_dir():
        shutil.rmtree(dir_path)