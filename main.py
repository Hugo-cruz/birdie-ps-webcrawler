from selenium import webdriver
import json






def get_object_properties_single_page(url):
    driver = webdriver.Firefox()
    driver.get(url)
    datalayer = driver.execute_script('return dataLayer')
    driver.quit()
    return datalayer["products"][0]["productInfo"]


if __name__ == "__main__":
    product_info = get_object_properties_single_page("https://www.lowes.com/pd/Whirlpool-24-5-cu-ft-4-Door-French-Door-Refrigerator-with-Ice-Maker-Fingerprint-Resistant-Stainless-Steel-ENERGY-STAR/1000257811")
    print(product_info)
