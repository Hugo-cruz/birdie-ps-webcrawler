from selenium import webdriver
import json


def parse_product_dict(datalayer_product_info,url):
    product_info  = {
        "SKU": datalayer_product_info["productID"],
        "Título": datalayer_product_info["productName"],
        "URL":url
    }
    return product_info


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
    product_links = eliminate_duplicates(product_links)
    return product_links

def eliminate_duplicates(product_links):
    return list(dict.fromkeys(product_links))


def get_product_info(url):
    driver = webdriver.Firefox()
    driver.get(url)
    datalayer = driver.execute_script('return dataLayer')
    print(datalayer["products"][0]["productInfo"])
    driver.quit()
    
    return parse_product_dict(datalayer["products"][0]["productInfo"],url)

def get_subcategory_pages(url):
    subcategory_pages = []
    driver = webdriver.Firefox()
    driver.get(url)
    elements = driver.find_elements_by_class_name("grid-16")
    for element in elements:
        a_tag = element.find_element_by_css_selector("a[href]")
        subcategory_pages.append(a_tag.get_attribute('href'))
    driver.quit()
    subcategory_pages = eliminate_duplicates(subcategory_pages)
    return subcategory_pages

def merge_lists(base,list_to_append):
    [base.append(element) for element in list_to_append]
    return base


if __name__ == "__main__":
    product_info = get_product_info("https://www.lowes.com/pd/Whirlpool-24-5-cu-ft-4-Door-French-Door-Refrigerator-with-Ice-Maker-Fingerprint-Resistant-Stainless-Steel-ENERGY-STAR/1000257811")
    print(product_info)
    #print(product_info)
    #element = get_products_from_subcategory_page("https://www.lowes.com/pl/Side-by-side-refrigerators-Refrigerators-Appliances/4294857970")
    '''
    subcategory_pages = get_subcategory_pages("https://www.lowes.com/c/Refrigerators-Appliances")
    print(subcategory_pages)
    products = []
    for subcategory in subcategory_pages:
        print(subcategory)
        merge_lists(products,get_products_from_subcategory_page(subcategory))
        print(products)
    '''
    
    