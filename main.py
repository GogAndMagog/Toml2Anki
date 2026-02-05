import argparse

from anki_genearor import  DeckGenerator
from toml_loader import TomlLoader

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

    parser = argparse.ArgumentParser(description='Пример скрипта для чтения аргументов командной строки.')

    parser.add_argument('url', type=str, help='Ссылка на TOML, из репозитория')
    parser.add_argument('path', type=str, help='Папка, куда будет сохранена колода')

    args = parser.parse_args()

    toml = TomlLoader.get_from_url(args.url)
    DeckGenerator.generate_deck(args.path, toml)
