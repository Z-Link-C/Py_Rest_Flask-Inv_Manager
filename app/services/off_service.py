import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2/product"

def search_product(barcode):
    response = requests.get(f"{BASE_URL}/{int(barcode)}.json")
    if response.status_code == 200:
        return response.json().get("product")
    return None