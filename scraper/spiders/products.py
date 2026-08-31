from collections.abc import Iterator

import scrapy

from scraper.config import settings
from scraper.items import ProductItem
from scraper.pages import CategoryPage


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = [settings.domain]  # noqa: RUF012
    start_urls = settings.scraping_category_urls

    def parse(
        self,
        response,
        page: CategoryPage,
    ) -> Iterator[scrapy.Request]:

        yield from response.follow_all(
            page.product_urls,
            callback=self.parse_product,
        )

        if page.next_page_url:
            yield response.follow(
                page.next_page_url,
                callback=self.parse,
            )

    def parse_product(
        self,
        _response,
        item: ProductItem,
    ) -> Iterator[ProductItem]:
        yield item
