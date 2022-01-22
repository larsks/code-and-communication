import os
import requests
import urllib.parse
import sys

from typing import Any, Optional, Union

default_gutendex_baseurl = "https://gutendex.com/"


class Gutendex(requests.Session):
    def __init__(self, baseurl: Optional[str] = None):
        super().__init__()
        self.baseurl = baseurl or default_gutendex_baseurl

    def search(self, keywords: str) -> Any:
        res = self.get("/books", params={"search": keywords})
        res.raise_for_status()
        return res.json()

    def request(
        self, method: str, url: Union[str, bytes], *args, **kwargs
    ) -> requests.Response:

        # This mess is necessary to make mypy happy.
        _url = url.decode() if isinstance(url, bytes) else url

        if self.baseurl and not _url.startswith("http"):
            _url = urllib.parse.urljoin(self.baseurl, _url)

        return super().request(method, _url, *args, **kwargs)


def main() -> None:
    G = Gutendex()

    keywords = " ".join(sys.argv[1:])
    res = G.search(keywords)

    for item in res["results"]:
        print(item["title"])


if __name__ == "__main__":
    main()
