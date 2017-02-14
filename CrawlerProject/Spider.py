from urllib.request import urlopen
from CrawlerProject.linkFinder import LinkFinder
from CrawlerProject.general import *
from urllib.parse import urlparse

class Spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url = None, domain_name = None):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        self.testvalue = None

    @staticmethod
    def boot(self, val):
        Spider.queue.add(val)
        self.testvalue = val

    @staticmethod
    def crawl_page():
        Spider.gather_links('http://www.ifeng.com/')

    @staticmethod
    def gather_links(page_url = None):
        html_string = ""
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
                first10Lines = html_string.split('\n')[:10]
                print(first10Lines)
            domainval = urlparse(page_url).netloc
            print(domainval)
        except Exception as e:
            print(e)


s = Spider('test')
s.crawl_page()





