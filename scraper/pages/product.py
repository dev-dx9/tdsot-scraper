from web_poet import Returns, WebPage, field, handle_urls

from scraper.config import settings
from scraper.items import ProductItem


@handle_urls(f'{settings.site_url}/*')
class ProductPage(WebPage, Returns[ProductItem]):
    @field
    def source_url(self) -> str:
        return str(self.response.url)
