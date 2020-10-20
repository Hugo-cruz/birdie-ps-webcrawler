from selenium import webdriver
import json
import utils as utils

def get_products_from_subcategory_page(url):
    offset = 0
    product_links = []
    
    while True:
        driver = webdriver.Firefox()
        driver.get(url+"?offset="+str(offset))
        offset = offset=offset+36
        elements = driver.find_elements_by_css_selector('a[data-clicktype="product_tile_click"][href]')
        [product_links.append(elem.get_attribute('href')) for elem in elements]
        datalayer = driver.execute_script('return dataLayer')
        driver.quit()
        if(len(datalayer["products"])!=36):
            break
    product_links = utils.eliminate_duplicates(product_links)
    return product_links



def get_product_info(url):
    driver = webdriver.Firefox()
    driver.get(url)
    datalayer = driver.execute_script('return dataLayer')
    print(datalayer["products"][0]["productInfo"])
    driver.quit()
    
    return utils.parse_product_dict(datalayer["products"][0]["productInfo"],url)

def get_subcategory_pages(url):
    subcategory_pages = []
    driver = webdriver.Firefox()
    driver.get(url)
    elements = driver.find_elements_by_class_name("grid-16")
    for element in elements:
        a_tag = element.find_element_by_css_selector("a[href]")
        subcategory_pages.append(a_tag.get_attribute('href'))
    driver.quit()
    subcategory_pages = utils.eliminate_duplicates(subcategory_pages)
    return subcategory_pages

