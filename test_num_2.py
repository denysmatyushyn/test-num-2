import urllib.request
import re

search_phrase_1 = r"PHP Version"
search_phrase_2 = r"Hi Denis"
url_first = "http://matiushyn.dev.run//"
url_second = "http://matiushyn.dev.run/?arg=Denis"


def test_scraper(check_url, search_phrase):
    page_scraper = urllib.request.urlopen(check_url).read()
    search_results = re.findall(search_phrase, str(page_scraper))
    print(search_results)
    if search_results:
        print("Test passed")
    else:
        print("Test no passed")


test_scraper(url_first, search_phrase_1)
test_scraper(url_second, search_phrase_2)