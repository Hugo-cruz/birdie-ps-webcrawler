
def parse_product_dict(datalayer_product_info,url):
    product_info  = {
        "SKU": datalayer_product_info["productID"],
        "Título": datalayer_product_info["productName"],
        "URL":url
    }
    return product_info

def eliminate_duplicates(product_links):
    return list(dict.fromkeys(product_links))

def merge_lists(base,list_to_append):
    [base.append(element) for element in list_to_append]
    return base