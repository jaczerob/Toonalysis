from typing import Any
import json
import sys
import re

import requests

from toonalysis import static
from toonalysis.types import Toon


regex = re.compile(static.SCRAPER_REGEX_PATTERN)
user_agent = 'Toonalysis Python/{0[0]}.{0[1]} aiohttp/{1}'.format(sys.version_info, requests.__version__)
headers = {'User-Agent': user_agent}


class Scraper:
    def __init__(self) -> None:
        self._session = requests.Session()

    def _get_groups(self) -> dict | None:
        with self._session.get(static.SCRAPER_URL, headers=headers) as resp:
            if not (match := regex.search(str(resp.content).replace('\\', '\\\\'))):
                return None

            state = json.loads(match.group(1))
            groups = filter(lambda group: group["game"] == 1, state["groups"])
            return groups
            
    def get_toons(self) -> list[Toon]:
        groups = self._get_groups()
        if groups is None:
            return []

        toons = []
        for group in groups:
            for member in group["members"]:
                toon: dict[str, Any] = member["toon"]
                if toon["game"] == 2:
                    continue

                is_sync = bool(toon["photo_bg"])
                organic = " ".join(toon.pop("prestiges"))

                if organic == "" and is_sync:
                    organic = static.SCRAPER_SYNCED_DEFAULT_ORGANIC
                elif organic == "" and not is_sync:
                    organic = static.SCRAPER_UNSYNCED_DEFAULT_ORGANIC

                toon["organic"] = organic
                toons.append(Toon(**toon))

        return toons


    def __enter__(self):
        return self

    def __exit__(self, *_):
        self._session.close()
