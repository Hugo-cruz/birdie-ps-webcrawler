from selenium import webdriver
import json
import crawler_functions as crawler
import utils as utils

refrigerator_page = 'https://www.lowes.com/c/Refrigerators-Appliances'


if __name__ == "__main__":
    
    subcategory_pages = crawler.get_subcategory_pages(refrigerator_page)
    products = []
    for subcategory in subcategory_pages:
        utils.merge_lists(products,crawler.get_products_from_subcategory_page(subcategory))
    product_list = []
    for product in products:
        product_list.append(crawler.get_product_info(product))
    
    
    