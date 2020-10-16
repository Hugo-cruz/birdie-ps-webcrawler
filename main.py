from selenium import webdriver
import json


def get_products_from_subcategory_page(url):
    offset = 0
    
    while True:
        driver = webdriver.Firefox()
        driver.get(url+"?offset="+str(offset))
        offset=offset+36
        elements = driver.find_elements_by_css_selector('a[data-clicktype="product_tile_click"][href]')
        product_links = [elem.get_attribute('href') for elem in elements]
        product_links = list( dict.fromkeys(product_links) )
        print(len(product_links))
        datalayer = driver.execute_script('return dataLayer')
        driver.quit()
        if(len(datalayer["products"])!=36):
            break



def get_object_properties_single_page(url):
    driver = webdriver.Firefox()
    driver.get(url)
    datalayer = driver.execute_script('return dataLayer')
    driver.quit()
    return datalayer["products"][0]["productInfo"]


if __name__ == "__main__":
    #product_info = get_object_properties_single_page("https://www.lowes.com/pd/Whirlpool-24-5-cu-ft-4-Door-French-Door-Refrigerator-with-Ice-Maker-Fingerprint-Resistant-Stainless-Steel-ENERGY-STAR/1000257811")
    #print(product_info)
    element = get_products_from_subcategory_page("https://www.lowes.com/pl/Side-by-side-refrigerators-Refrigerators-Appliances/4294857970")
    
