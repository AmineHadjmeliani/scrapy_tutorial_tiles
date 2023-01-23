# scrapy tutorial tiles

This Python tutorial is designed for individuals new to Scrapy. It covers the basics of crawling with a basic spider and guides you through creating a complete tutorial project, including exporting data to a CSV file. The tutorial will show you how to scrape product names and prices from an online shop. Additionally, you will learn how to use the Scrapy shell to parse data, extract text and href attributes from HTML, and scrape multiple pages. This is a comprehensive guide on how to create your first Scrapy spider project using Python3.


In this script we would be using the `Scrapy` library to scrape data from the website magnatiles.com. The script defines a class TilesSpider which is a subclass of `scrapy.Spider`. The spider has a name 'tiles', allowed_domains of ['magnatiles.com'] and start_urls of ['http://magnatiles.com/products/page/1/'].

In the parse method, the script iterates through each element "ul.products li" in the HTML response, using the CSS selector. For each iteration, it creates an ItemLoader object named "il" with an instance of the custom class SpidertilesItem() as the item and the current iteration as the selector.

Then, it uses the add_css method to extract the following information from the current iteration:

sku: the value of the 'data-product_sku' attribute of the 'a.button' element
name: the text of the `h2`element
price: the text of the `bdi` element
Finally, it yields the loaded item using `il.load_item()` method.

This script is scraping the sku, name and price of the products from the website magnatiles.com using the css selectors and loading the scraped data in the `SpidertilesItem` object.