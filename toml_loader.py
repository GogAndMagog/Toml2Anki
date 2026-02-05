import tomllib
import urllib.request

class TomlLoader:

    @staticmethod
    def get_from_url(url: str) -> dict:
        file = urllib.request.urlopen(url).read()
        return tomllib.loads(file.decode("utf-8"))
