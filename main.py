from anki_genearor import  DeckGenerator
from toml_loader import TomlLoader

URL = r"https://raw.githubusercontent.com/zhukovsd/java-backend-interview-prep/refs/heads/master/data/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20Java/Collections.toml"
DESTINATION = r"C:/Users/user/PycharmProjects/Toml2Anki/Test"
PICTURE_URL = r"/java-backend-interview-prep/hibernate_entity_life_cycle.png"
PICTURES_SOURCE = r"https://zhukovsd.github.io"

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

    toml = TomlLoader.get_from_url(URL)
    DeckGenerator.generate_deck(DESTINATION, toml)
