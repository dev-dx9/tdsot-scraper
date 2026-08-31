import re
from urllib.parse import urljoin

from web_poet import Returns, WebPage, field, handle_urls

from scraper.config import settings
from scraper.items import ProductItem
from scraper.selectors import (
    PRODUCT_ATTRIBUTE_NAME,
    PRODUCT_ATTRIBUTE_VALUE,
    PRODUCT_ATTRIBUTES,
    PRODUCT_BRAND,
    PRODUCT_CATEGORY,
    PRODUCT_CURRENCY,
    PRODUCT_DESCRIPTION,
    PRODUCT_IMAGE_URLS,
    PRODUCT_NAME,
    PRODUCT_PRICE,
    PRODUCT_SKU,
    PRODUCT_SKU_LABEL,
)


@handle_urls(f'{settings.site_url}/*')
class ProductPage(WebPage, Returns[ProductItem]):
    def _get_value(self, selector: str) -> str | None:
        value = self.response.css(selector).get()
        return value.strip() if value is not None else None

    @staticmethod
    def _get_original_image_url(url: str) -> str:
        return re.sub(
            r'/resize-cache/(iblock/.+?)/\d+-\d+-[^/]+/',
            r'/\1/',
            url,
        )

    @staticmethod
    def _clean_description(node) -> str:
        for element in node.xpath(
            './/*[@style or @align or @width or @height or @border]'
        ):
            for attribute in ('style', 'align', 'width', 'height', 'border'):
                element.attrib.pop(attribute, None)

        return (
            ''.join(node.xpath('./node()').getall())
            .translate(str.maketrans('', '', '\n\r\t'))
            .strip()
        )

    @field
    def source_url(self) -> str:
        return str(self.response.url)

    @field
    def name(self) -> str | None:
        return self._get_value(PRODUCT_NAME)

    @field
    def category(self) -> str | None:
        value = self._get_value(PRODUCT_CATEGORY)

        if not value:
            return None

        return '/'.join(' '.join(category.split()) for category in value.split('/'))

    @field
    def brand(self) -> str | None:
        value = self._get_value(PRODUCT_BRAND)

        if not value or value == '<не указан>':
            return None

        return value

    @field
    def sku(self) -> str | None:
        value = self._get_value(PRODUCT_SKU)

        if value is None:
            return None

        return value.removeprefix(PRODUCT_SKU_LABEL).strip() or None

    @field
    def price(self) -> str | None:
        return self._get_value(PRODUCT_PRICE)

    @field
    def currency(self) -> str | None:
        return self._get_value(PRODUCT_CURRENCY)

    import re

    @field
    def description(self) -> str | None:
        description = self.response.css(PRODUCT_DESCRIPTION)

        if not description:
            return None

        return self._clean_description(description)

    @field
    def image_urls(self) -> list[str]:
        image_urls = self.response.css(PRODUCT_IMAGE_URLS).getall()

        return [
            self._get_original_image_url(urljoin(str(self.response.url), url))
            for url in image_urls
            if url.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
        ]

    @field
    def attributes(self) -> dict[str, str]:
        attributes = {}

        for attribute in self.css(PRODUCT_ATTRIBUTES):
            name = attribute.css(PRODUCT_ATTRIBUTE_NAME).get()
            value = attribute.css(PRODUCT_ATTRIBUTE_VALUE).get()

            if name and value:
                attributes[name.strip().rstrip(':')] = value.strip()

        return attributes
