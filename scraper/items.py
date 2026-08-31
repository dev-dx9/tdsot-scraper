# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass


@dataclass
class ProductItem:
    source_url: str
    name: str | None
    category: str | None
    brand: str | None
    sku: str | None
    price: str | None
    currency: str | None
    description: str | None
    image_urls: list[str]
    attributes: dict[str, str]
    documents: list[str]
