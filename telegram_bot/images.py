import random
from typing import Set, List

import requests


def get_random_image() -> str:
    choice = random.choice(get_dirty())
    print(choice)

    return choice


def get_dirty() -> List[str]:
    import re

    links = set()
    response = requests.get("https://photos.google.com/share/AF1QipNS94mSZRF81m0SaNwqEe5FvV3aQ0Zm9zbOp-HNg6s5EU4upTuqnrZj2-_VSyLn8Q?key=Qk9VUDlXVHZqRGtWOFo1aUxVXzdReElsU2NuNExR")
    content = response.content.decode("utf-8")
    for find in re.findall('"(https://lh3.googleusercontent.com/[^"]+)"', content):
        if 'https://lh3.googleusercontent.com/a/' in find or find == "https://lh3.googleusercontent.com/YhfpzamTTNKpbiVWUZjP8T0URrfTdxD-iQS0iy1Q00vPYgpYP-TvTGpsXlpjNXGcZd9kC_SC_pF4kWbHRwpHXpqXLH5QjEocn6-HpkSiDqOf":
            continue
        links.add(find)

    return list(links)
