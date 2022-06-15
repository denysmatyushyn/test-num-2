import urllib.request
import re

url_first = 'http://matiushyn.dev.run//'
search_phrase_1 = r"PHP Version"

url_second = 'http://matiushyn.dev.run/?arg='
search_phrase_2 = r'Hi '
payload = ['Denis', 'Akim', 'Sany']


def test_scraper(check_url, search_phrase):
    page_scraper = urllib.request.urlopen(check_url).read()
    search_results = re.findall(search_phrase, str(page_scraper))
    print(search_results)
    if search_results:
        print("Test passed")
    else:
        print("Test no passed")


test_scraper(url_first, search_phrase_1)
for x in payload:
    print(url_second+x, search_phrase_2+x)
    test_scraper(url_second+x, search_phrase_2+x)