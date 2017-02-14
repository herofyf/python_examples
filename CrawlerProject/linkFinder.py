from html.parser import HTMLParser

from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url = None):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

finder = LinkFinder('http://www.ifeng.com', '')
'''
finder.feed('<html><head><title>tewst</title></head'
            '<body><h1>parse me !</h1></body></html>')
'''

finder.feed('<html></html>')

