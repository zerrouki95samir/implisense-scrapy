import scrapy
import sqlite3
import time

def create_database():
    conn = sqlite3.connect('implisense.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS company_urls (
            id INTEGER PRIMARY KEY,
            url TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

class ImplisenseSpider(scrapy.Spider):
    name = 'implisense'
    allowed_domains = ['implisense.com']
    start_urls = ['https://implisense.com/de']
    max_depth = 14
    request_delay = 0.5

    def __init__(self, *args, **kwargs):
        super(ImplisenseSpider, self).__init__(*args, **kwargs)
        create_database()
        self.conn = sqlite3.connect('implisense.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def parse(self, response):
        depth = response.meta.get('depth', 1)
        if depth > self.max_depth:
            return

        time.sleep(self.request_delay)
        
        for link in response.css('a::attr(href)').getall():
            full_url = response.urljoin(link)
            if self.is_company_url(full_url) and not self.url_exists(full_url):
                self.add_url(full_url)
                yield {'url': full_url}
            elif self.should_follow_link(full_url):
                yield response.follow(link, self.parse, meta={'depth': depth + 1})
                

    def is_company_url(self, url):
        return "/de/companies/" in url and not url.startswith("https://api.whatsapp.com/send?text=") 

    
    def should_follow_link(self, url):
        unwanted_keywords = ["login", "pricing", "subscriptions", "referer"]
        return all(keyword not in url for keyword in unwanted_keywords) and self.is_internal_url(url)
    
    def url_exists(self, url):
        url_without_fragment_query = url.split('#')[0].split('?')[0]
        self.cursor.execute('SELECT id FROM company_urls WHERE url = ?', (url_without_fragment_query,))
        return self.cursor.fetchone() is not None

    def add_url(self, url):
        url_without_fragment_query = url.split('#')[0].split('?')[0]
        self.cursor.execute('INSERT OR IGNORE INTO company_urls (url) VALUES (?)', (url_without_fragment_query,))
        self.conn.commit()

    def closed(self, reason):
        self.conn.close()

    def is_internal_url(self, url):
        return url.startswith(self.start_urls[0])

if __name__ == "__main__":
    create_database()