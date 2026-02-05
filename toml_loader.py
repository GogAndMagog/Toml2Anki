import tomllib
import urllib.request

def load_toml(url: str) -> dict:

    file = urllib.request.urlopen(url).read()
    toml = tomllib.loads(file.decode("utf-8"))

    return toml