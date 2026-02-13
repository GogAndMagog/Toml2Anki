import argparse

from anki_genearor import  DeckGenerator
from toml_loader import TomlLoader

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

    parser = argparse.ArgumentParser(description='Пример скрипта для чтения аргументов командной строки.')

    parser.add_argument('url', type=str, help='Ссылка на TOML, из репозитория')
    parser.add_argument('anki_path', type=str, help='Папка, куда будет сохранена колода')
    parser.add_argument('--pictures_path', type=str, help='Папка, куда будет сохранена колода')

    args = parser.parse_args()

    pictures_path = args.anki_path if args.pictures_path is None else args.pictures_path

    toml = TomlLoader.get_from_url(args.url)
    DeckGenerator.generate_deck(args.anki_path, pictures_path, toml)
