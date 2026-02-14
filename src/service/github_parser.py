import requests

from pathlib import Path
from urllib.parse import quote

class GithubParser:

    @staticmethod
    def parse(owner, repo, sha, toml_folder) -> list:

        api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{sha}?recursive=%22true%22"

        response = requests.get(api_url)
        paths = []

        if response.status_code != 200:
            return paths

        for item in response.json()['tree']:
            if item['path'].startswith(toml_folder + '/') and item['path'].endswith('.toml'):
                # Выделение промежуточного пути между папкой c TOML-ами и конкретным файлом
                intermediate_path = Path(item['path']).parts[1:-1]
                download_url = GithubParser.__get_download_url(owner, repo, item['path'])
                paths.append((intermediate_path[0] if intermediate_path else None, download_url))

        return paths

    @staticmethod
    def __get_download_url(owner, repo, path) -> str:
        # Нужно для перобразования кириллицы к URL-виду
        encoded_path = quote(path)
        download_url = f"https://raw.githubusercontent.com/{owner}/{repo}/master/{encoded_path}"
        return download_url