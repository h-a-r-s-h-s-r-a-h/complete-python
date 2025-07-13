import threading
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from collections import deque
import re

class WebsiteScraper:
    def __init__(self, base_url, max_workers=10, max_pages=100, delay=0.1):
        self.base_url = base_url
        self.base_domain = urlparse(base_url).netloc
        self.max_workers = max_workers
        self.max_pages = max_pages
        self.delay = delay
        
        # Thread-safe data structures
        self.visited_urls = set()
        self.urls_to_visit = deque([base_url])
        self.scraped_data = {}
        self.failed_urls = []
        
        # Threading locks
        self.url_lock = threading.Lock()
        self.data_lock = threading.Lock()
        
        # Session for connection pooling
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def is_valid_url(self, url):
        """Check if URL is valid and belongs to the same domain"""
        try:
            parsed = urlparse(url)
            return (parsed.netloc == self.base_domain and 
                   parsed.scheme in ['http', 'https'] and
                   not any(ext in url.lower() for ext in ['.pdf', '.jpg', '.png', '.gif', '.css', '.js', '.zip', '.doc']))
        except:
            return False
    
    def get_next_url(self):
        """Thread-safe method to get next URL to scrape"""
        with self.url_lock:
            if self.urls_to_visit and len(self.visited_urls) < self.max_pages:
                url = self.urls_to_visit.popleft()
                if url not in self.visited_urls:
                    self.visited_urls.add(url)
                    return url
        return None
    
    def add_urls(self, urls):
        """Thread-safe method to add new URLs"""
        with self.url_lock:
            for url in urls:
                if url not in self.visited_urls and url not in self.urls_to_visit:
                    self.urls_to_visit.append(url)
    
    def extract_links(self, soup, current_url):
        """Extract all links from the page"""
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(current_url, href)
            if self.is_valid_url(full_url):
                links.append(full_url)
        return links
    
    def scrape_page(self, url):
        """Scrape a single page"""
        try:
            print(f"🔍 Scraping: {url}")
            
            # Add delay to be respectful
            time.sleep(self.delay)
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract content
            title = soup.find('title')
            title_text = title.get_text().strip() if title else "No Title"
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text content
            text_content = soup.get_text()
            clean_text = re.sub(r'\s+', ' ', text_content).strip()
            
            # Extract meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            description = meta_desc.get('content', '') if meta_desc else ''
            
            # Extract headings
            headings = []
            for i in range(1, 7):
                for heading in soup.find_all(f'h{i}'):
                    headings.append({
                        'level': i,
                        'text': heading.get_text().strip()
                    })
            
            # Store scraped data
            page_data = {
                'url': url,
                'title': title_text,
                'description': description,
                'content': clean_text,
                'content_length': len(clean_text),
                'headings': headings,
                'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            with self.data_lock:
                self.scraped_data[url] = page_data
            
            # Extract and add new links
            links = self.extract_links(soup, url)
            self.add_urls(links)
            
            print(f"✅ Scraped: {url} ({len(clean_text)} chars, {len(links)} links found)")
            return page_data
            
        except Exception as e:
            print(f"❌ Failed to scrape {url}: {str(e)}")
            with self.data_lock:
                self.failed_urls.append({'url': url, 'error': str(e)})
            return None
    
    def worker(self):
        """Worker thread function"""
        while True:
            url = self.get_next_url()
            if url is None:
                break
            self.scrape_page(url)
    
    def scrape_website(self):
        """Main method to scrape entire website"""
        print(f"🚀 Starting to scrape website: {self.base_url}")
        print(f"⚙️  Configuration: {self.max_workers} workers, max {self.max_pages} pages, {self.delay}s delay")
        
        start_time = time.time()
        
        # Use ThreadPoolExecutor for better thread management
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit worker tasks
            futures = [executor.submit(self.worker) for _ in range(self.max_workers)]
            
            # Wait for all workers to complete
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Worker error: {e}")
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\n📊 Scraping Summary:")
        print(f"   Total pages scraped: {len(self.scraped_data)}")
        print(f"   Failed URLs: {len(self.failed_urls)}")
        print(f"   Total time: {duration:.2f} seconds")
        print(f"   Average time per page: {duration/len(self.scraped_data):.2f} seconds")
        
        return self.scraped_data
    
    def save_data(self, filename=None):
        """Save scraped data to JSON file"""
        if filename is None:
            domain = self.base_domain.replace('.', '_')
            filename = f"scraped_{domain}_{int(time.time())}.json"
        
        data_to_save = {
            'scraping_info': {
                'base_url': self.base_url,
                'total_pages': len(self.scraped_data),
                'failed_urls': len(self.failed_urls),
                'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
            },
            'pages': self.scraped_data,
            'failed_urls': self.failed_urls
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Data saved to: {filename}")
        return filename
    
    def get_summary(self):
        """Get summary of scraped data"""
        total_content = sum(len(data['content']) for data in self.scraped_data.values())
        
        summary = {
            'total_pages': len(self.scraped_data),
            'total_characters': total_content,
            'failed_urls': len(self.failed_urls),
            'average_page_size': total_content // len(self.scraped_data) if self.scraped_data else 0,
            'pages_by_size': sorted(
                [(url, len(data['content'])) for url, data in self.scraped_data.items()],
                key=lambda x: x[1], reverse=True
            )[:10]  # Top 10 largest pages
        }
        
        return summary

# Example usage and convenience function
def scrape_website_fast(url, max_workers=15, max_pages=200, delay=0.1, save_to_file=True):
    """
    Quick function to scrape a website with optimal settings
    
    Args:
        url: Website URL to scrape
        max_workers: Number of concurrent threads (default: 15)
        max_pages: Maximum pages to scrape (default: 200)
        delay: Delay between requests in seconds (default: 0.1)
        save_to_file: Whether to save results to JSON file (default: True)
    
    Returns:
        Dictionary with scraped data
    """
    scraper = WebsiteScraper(url, max_workers=max_workers, max_pages=max_pages, delay=delay)
    scraped_data = scraper.scrape_website()
    
    if save_to_file:
        scraper.save_data()
    
    # Print summary
    summary = scraper.get_summary()
    print(f"\n📈 Summary:")
    print(f"   📄 Total pages: {summary['total_pages']}")
    print(f"   📝 Total characters: {summary['total_characters']:,}")
    print(f"   📊 Average page size: {summary['average_page_size']:,} characters")
    print(f"   ❌ Failed URLs: {summary['failed_urls']}")
    
    return scraped_data

# Example usage
if __name__ == "__main__":
    # Example 1: Quick scraping
    # print("Example 1: Quick scraping")
    # data = scrape_website_fast("https://devstream.org/", max_workers=10, max_pages=50)
    
    # Example 2: Custom scraper with more control
    print("\nExample 2: Custom scraper")
    scraper = WebsiteScraper("https://metabees.org/", max_workers=8, max_pages=30, delay=0.2)
    scraped_data = scraper.scrape_website()
    scraper.save_data()
    
    # Display some results
    print("\n🎯 Sample scraped pages:")
    for i, (url, data) in enumerate(list(scraped_data.items())[:3]):
        print(f"\n{i+1}. {data['title']}")
        print(f"   URL: {url}")
        print(f"   Content: {data['content'][:200]}...")
        print(f"   Size: {data['content_length']} characters")