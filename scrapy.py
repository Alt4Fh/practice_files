import threading
import queue
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


class Urls(threading.Thread):
    def __init__(self, q: queue.Queue, url: str):
        super().__init__()
        self.q = q
        self.url = url
        self.cat_links = []  # Instance-level variable to store links
    
    def request_url(self) -> BeautifulSoup | None:
        """Request the URL and return the parsed BeautifulSoup object."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }
        try:
            res = requests.get(self.url, headers=headers)
            res.raise_for_status()  # Raise an HTTPError for bad responses
            return BeautifulSoup(res.text, 'lxml')
        except requests.RequestException as e:
            print(f"Error fetching {self.url}: {e}")
            return None
    
    def get_category_links(self, soup: BeautifulSoup) -> list[str]:
        """Extract category links from the page."""
        cat_links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and '/categories/' in href:
                full_url = f"https://www.1mg.com{href}"
                cat_links.append(full_url)
        return cat_links

    def run(self):
        """Main thread execution."""
        soup = self.request_url()
        if soup:
            self.cat_links = self.get_category_links(soup)
            self.q.put(self.cat_links)  # Return the results via the queue


def fetch_category_links(url: str) -> list[str]:
    """Fetch category links from the given URL."""
    q = queue.Queue()
    thread = Urls(q, url)
    thread.start()
    thread.join()
    return q.get()


def fetch_sub_category_links(cat_links: list[str]) -> list[list[str]]:
    """Fetch sub-category links for each category link."""
    all_sub_links = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(fetch_category_links, link) for link in cat_links]
        for future in futures:
            all_sub_links.append(future.result())
    return all_sub_links


def main():
    base_url = 'https://www.1mg.com/'
    
    # Fetch category links from the base URL
    cat_links = fetch_category_links(base_url)
    print(f"Found {len(cat_links)} category links.")

    # Now, fetch sub-category links for each category
    sub_category_links = fetch_sub_category_links(cat_links)
    for links in sub_category_links:
        print(f'num of links: {len(links)}')


if __name__ == '__main__':
    main()
