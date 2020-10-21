import utils as utils
import crawler_functions as crawler



def test_get_product_info():

    test_produc_info = {
        'SKU': '1000257811', 
        'Título': '24.5-cu_ft_4-door_36-in_french_door_refrigerator_with_exterior_ice_and_water_dispenser_-_fingerprint_resistant_stainless_steel', 
        'URL': 'https://www.lowes.com/pd/Whirlpool-24-5-cu-ft-4-Door-French-Door-Refrigerator-with-Ice-Maker-Fingerprint-Resistant-Stainless-Steel-ENERGY-STAR/1000257811'
    }
    assert crawler.get_product_info(test_produc_info["URL"]) == test_produc_info

def test_get_category_pages():
    category_0 = 'https://www.lowes.com/pl/French-door-refrigerators-Refrigerators-Appliances/4294857963'
    assert crawler.get_subcategory_pages('https://www.lowes.com/c/Refrigerators-Appliances')[0] == category_0