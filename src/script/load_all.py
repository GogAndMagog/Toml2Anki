import tomllib
import argparse
import os
import zipfile

from src.service.github_parser import GithubParser

from src.service.anki_genearor import  DeckGenerator
from src.service.toml_loader import TomlLoader
from urllib.parse import quote

if __name__ == '__main__':
    # Загрузка конфига
    with open("config.toml", "rb") as config_file:
        config = tomllib.load(config_file)
    owner = config['app']['owner']
    repo = config['app']['repo']
    sha = config['app']['sha']
    toml_folder = config['app']['toml_folder']
    exclude_tomls = config['app']['exclude_tomls']
    destination_directory = config['app']['destination_directory']

    parser = argparse.ArgumentParser(description='Парсер аргументов командной строки.')

    parser.add_argument('--owner', type=str, help='Владелец репозитория', default=owner)
    parser.add_argument('--repo', type=str, help='Репозиторий', default=repo)
    parser.add_argument('--sha', type=str, help='', default=sha)
    parser.add_argument('--toml_folder', type=str, help='Папка, где находятся файлы с .toml', default=toml_folder)
    parser.add_argument('--exclude_tomls', nargs="*", help='Файлы .toml, которые надо проигнорировать', default=exclude_tomls)
    parser.add_argument('--destination_directory', type=str, help='Папка, куда колоды будут сохранены', default=destination_directory)
    parser.add_argument('--archive', action="store_true", help='Флаг, указывает о необходимости создания архива с колодами')

    args = parser.parse_args()

    toml_paths = GithubParser.parse(args.owner, args.repo, args.sha, args.toml_folder)

    encoded_exclude_tomls = []

    for exclude_toml in args.exclude_tomls:
        encoded_exclude_tomls.append(quote(exclude_toml))

    # Загрузка и генерирование Anki-колод
    for toml_path in toml_paths:
        if not any(pattern in toml_path[1] for pattern in encoded_exclude_tomls):
            toml = TomlLoader.get_from_url(toml_path[1])
            DeckGenerator.generate_deck(args.destination_directory + '\\' + toml_path[0], args.destination_directory, toml)

    # Архивирование папки, если нужно
    if args.archive:
        archive_path = args.destination_directory + "\\AnkiDeck.zip"
        with zipfile.ZipFile(archive_path, "w") as z:
            for root, dirs, files in os.walk(args.destination_directory):
                for file in files:
                    full_path = str(os.path.join(root, file))

                    if archive_path == full_path:
                        continue

                    relative_path = os.path.relpath(full_path, args.destination_directory)
                    z.write(full_path, arcname=relative_path)