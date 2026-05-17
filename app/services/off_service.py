import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2/product/"

def search_product(barcode):
    response = requests.get(f"{BASE_URL}{barcode}",
                        headers={"User-Agent": "food-inventory-app/1.0"})
    if response.status_code == 200:
        d=response.json()
        if d.get("status")==1:
            return d.get("product")
    return None
##3017624010701 is a good tester