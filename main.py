import time
from asyncio import wait
from pathlib import Path

from anki_genearor import generate_deck
from picture_loader import download_picture, delete_pictures_dir, PictureHandler
from toml_loader import load_toml

URL = r"https://raw.githubusercontent.com/zhukovsd/java-backend-interview-prep/refs/heads/master/data/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20Java/Collections.toml"
DESTINATION = r"C:/Users/user/PycharmProjects/Toml2Anki"
PICTURE_URL = r"/java-backend-interview-prep/hibernate_entity_life_cycle.png"

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
    # toml = load_toml(URL)
    # generate_deck(toml)
    picture_handler = PictureHandler()
    picture_handler.download_picture(DESTINATION, PICTURE_URL)
    picture_handler.delete_pictures_dir(DESTINATION)
    # print(download_picture(DESTINATION, r"/java-backend-interview-prep/hibernate_entity_life_cycle.png"))
    # time.sleep(1)
    # delete_pictures_dir(DESTINATION)
