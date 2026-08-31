CATEGORY_PRODUCT_URL = (
    '.prod-list__item[data-entity="item"] a[itemprop="url"]::attr(href)'
)

CATEGORY_NEXT_PAGE_URL = '.pagination a:contains("След.")::attr(href)'
PRODUCT_NAME = '.prod-detail meta[itemprop="name"]::attr(content)'
PRODUCT_CATEGORY = '.prod-detail meta[itemprop="category"]::attr(content)'
PRODUCT_BRAND = '.prod-detail [itemprop="brand"]::text'
PRODUCT_SKU = '.prod-detail-articul::text'
PRODUCT_SKU_LABEL = 'Артикул:'
PRODUCT_PRICE = '.prod-detail [itemprop="offers"] [itemprop="price"]::attr(content)'
PRODUCT_CURRENCY = (
    '.prod-detail [itemprop="offers"] [itemprop="priceCurrency"]::attr(content)'
)
PRODUCT_DESCRIPTION = '.prod-detail [itemprop="description"]'
PRODUCT_IMAGE_URLS = '.prod-detail [itemprop="image"]::attr(src)'
PRODUCT_ATTRIBUTES = '.prod-detail .detail-props__list .props-list__item'
PRODUCT_ATTRIBUTE_NAME = '.props-list__label ::text'
PRODUCT_ATTRIBUTE_VALUE = '.props-list__value ::text'
PRODUCT_DOCUMENTS = (
    '//div[contains(@class, "sec")][.//h2[normalize-space()="Документация"]]'
    '//li[contains(@class, "depth-level-1")]'
)
PRODUCT_DOCUMENT_URL = '.depth-level-2 .doc-cert__name::attr(href)'
