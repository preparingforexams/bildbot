import random
from typing import List

import requests


def get_random_image() -> str:
    choice = random.choice(get_dirty())
    print(choice)

    return choice


def get_dirty() -> List[str]:
    import re

    links = set()
    response = requests.get(
        "https://photos.google.com/share/AF1QipNS94mSZRF81m0SaNwqEe5FvV3aQ0Zm9zbOp-HNg6s5EU4upTuqnrZj2-_VSyLn8Q?key=Qk9VUDlXVHZqRGtWOFo1aUxVXzdReElsU2NuNExR")
    content = response.content.decode("utf-8")
    for find in re.findall('<img([^>]*)', content):
        link = re.search('(https://lh3.googleusercontent.com/[^"]+)', find).group()
        link = re.sub(r"=w\d+-h\d+(:?-no)?", "", link)
        link = re.sub(r"=s\d+(:?-no)?", "", link)
        if 'https://lh3.googleusercontent.com/a/' in link or (
                'width="32"' in find[0] and 'height="32"' in find[0]) or "title" in find:
            continue

        links.add(link)

    return list(links)
