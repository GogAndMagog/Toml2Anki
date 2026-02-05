import shutil
import urllib.request
from pathlib import Path

class PictureHandler:

    __PICTURES_DESTINATION = r"pictures"
    __PICTURES_SOURCE = r"https://zhukovsd.github.io"

    @staticmethod
    def download_picture_from_internet(destination: str, path: str) -> str:
        data = (urllib.request
                .urlopen(PictureHandler.__PICTURES_SOURCE + path)
                .read())
        dir_path = Path(destination) / PictureHandler.__PICTURES_DESTINATION / path.lstrip('/')
        dir_path.parent.mkdir(parents=True, exist_ok=True)
        dir_path.write_bytes(data)

        return str(dir_path)

    @staticmethod
    def delete_pictures_dir(destination: str):
        dir_path = Path(destination) / PictureHandler.__PICTURES_DESTINATION
        if dir_path.exists() and dir_path.is_dir():
            shutil.rmtree(dir_path)

