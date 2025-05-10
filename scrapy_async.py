#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
 Script Name   : scrapy_async.py
 Author        : Altaf husen
 Created       : 2025-05-02
 Description   : Fetches the 1mg homepage with custom headers using aiohttp.
===============================================================================
"""


import asyncio
from bs4 import BeautifulSoup
from typing import List
import json
import aiohttp
from urllib.parse import urljoin, urlparse


HEADERS = {
    ":authority": "www.1mg.com",
    ":method": "GET",
    ":path": "/",
    ":scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, zstd",
    "accept-language": "en-US,en;q=0.9,en-IN;q=0.8",
    "cache-control": "max-age=0",
    "cookie": "VISITOR-ID=c95b879d-ac9e-428d-85eb-011318bfb0d2_hGj2FwCu9J_8480_1746076877012; city=Gurgaon; abVisitorId=686919; abExperimentShow=true; jarvis-id=10e2c094-1e0d-401e-bfee-76c936af2529; ... [TRUNCATED FOR BREVITY]",
    "priority": "u=0, i",
    "sec-ch-ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}


# async def fetch_html(session: aiohttp.ClientSession, url:str ):
#     try:
#         async with session.get(url, headers=HEADERS) as resp:
#             print(f'response: {resp.status}')
#             html_data = await resp.text()
#             return html_data
#     except aiohttp.ClientError as e:
#         print(f"http request failed: {e}")

#         return None



# def extract_category_links(html: str) -> List[str]:
#     soup = BeautifulSoup(html, 'lxml')
#     links = []
#     for a in soup.find_all('a', href=True):
#         href = a['href']
#         if '/categories/' in href:
#             full_url = f"https://www.1mg.com{href}"
#             links.append(full_url)
#     return links


# async def get_category_links(session: aiohttp.ClientSession, url: str) -> List[str]:
#     html = await fetch_html(session, url)
#     if html:
#         return extract_category_links(html)
#     return []


# async def main():
#     base_url = "https://www.1mg.com/"

#     async with aiohttp.ClientSession() as session:
#         # Step 1: Get category links from base URL
#         print(f"Fetching main categories from {base_url} ...")
#         category_links = await get_category_links(session, base_url)
#         print(f"Found {len(category_links)} category links")

#         # Step 2: Get sub-category links from each category page
#         print(f"\nFetching sub-categories for {len(category_links)} categories...")
#         tasks = [get_category_links(session, url) for url in category_links]
#         sub_category_results = await asyncio.gather(*tasks)

#         # Optional: flatten all sub-links into one list
#         all_sub_links = [link for sublist in sub_category_results for link in sublist]

#         json_links = {"links" : []}

#         for i, sub_links in enumerate(sub_category_results):
#             print(f"\nCategory {i+1} has {len(sub_links)} sub-category links")
#             cat_links = {f"{i+1}" :  sub_links}
#             json_links["links"].append(cat_links)
#             # for link in sub_links:
#             #     print(link)

#         file_path = 'data.json'
#         with open(file_path, 'w') as json_file:
#             json.dump(json_links, json_file, indent=4)

#         print(f"JSON file created at {file_path}")
# # Entry point
# if __name__ == '__main__':
#     asyncio.run(main())



########----------------------------------------------------------------------------------------------------------------


class AsyncCrawler:
    def __init__(self, start_url, max_pages=10, max_depth=2, requests_per_minute=30):
        self.start_url = start_url
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.requests_per_minute = requests_per_minute
        self.delay = 60 / requests_per_minute
        self.visited = set() # Set to store visited URLs
        self.to_visit = [(start_url, 0)] # Queue of URLs to visit with depth
        self.domain = urlparse(start_url).netloc
        self.session = None

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def is_same_domain(self, url):
        return urlparse(url).netloc == self.domain

    async def fetch_page(self, session, url):
        try:
            async with session.get(url, headers = HEADERS, timeout=10) as response:
                if response.status == 200:
                    html = await response.text()
                    if response.history:
                        print(f"🔁 Redirected to {response.url}")
                    return html
                elif response.status == 404:
                    print(f"❌ 404 Not Found: {url}")
                else:
                    print(f"⚠️ HTTP {response.status} at {url}")
        except asyncio.TimeoutError:
            print(f"⏰ Timeout when accessing: {url}")
        except Exception as e:
            print(f"❗ Request failed for {url}: {e}")
        return None

    def extract_links(self, html, base_url):
        soup = BeautifulSoup(html, "html.parser")
        links = set()
        for tag in soup.find_all("a", href=True):
            href = urljoin(base_url, tag['href'])
            if self.is_valid_url(href) and self.is_same_domain(href):
                links.add(href)
        return links

    async def crawl(self):
        pages_crawled = 0

        async with aiohttp.ClientSession() as session:
            while self.to_visit and pages_crawled < self.max_pages:
                current_url, current_depth = self.to_visit.pop(0)

                if current_url in self.visited or current_depth > self.max_depth:
                    continue

                print(f"[{pages_crawled+1}] Depth {current_depth}: Crawling {current_url}")
                html = await self.fetch_page(session, current_url)
                if not html:
                    continue

                self.visited.add(current_url)
                pages_crawled += 1

                if current_depth < self.max_depth:
                    links = self.extract_links(html, current_url)
                    for link in links:
                        if link not in self.visited and all(link != u for u, _ in self.to_visit):
                            self.to_visit.append((link, current_depth + 1))

                # Rate limiting using async sleep
                await asyncio.sleep(self.delay)

# Example usage
if __name__ == "__main__":
    seed_url = "https://www.1mg.com/"
    crawler = AsyncCrawler(
        start_url=seed_url,
        max_pages=10,
        max_depth=2,
        requests_per_minute=20
    )
    asyncio.run(crawler.crawl())
