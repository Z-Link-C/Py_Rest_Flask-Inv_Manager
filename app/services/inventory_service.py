from .off_service import search_product
from app.db import db
def add_product(code,price,stock):
    prod_data=search_product(code)
    if not prod_data: return None, "Product not found in Database."
    
def get_all():
    return db

def get_one(id):
    return next((p for p in db if p["id"] == int(id)), None)

def add_product(code, price, stock):
    prod = search_product(code)
    if not prod:
        return None,"product not found"
    n_id = max((p["id"] for p in db),default=0)+1
    n_prod={
        "id":n_id,
        "barcode":code,
        "name":prod.get("product_name","Unknown"),
        "price":price,
        "stock":stock
    }
    db.append(n_prod)
    return n_prod,None

def update_product(id,price=None,stock=None):
    prod=get_one(id)
    if not prod:
        return None,f"Product {id} not found"
    if price is not None:
        prod["price"]=price
    if stock is not None:
        prod["stock"]=stock
    for p in db:
        if p["id"]==id:
            p.update({"price":price,"stock":stock})
    return prod,None

def delete_product(id):
    prod=get_one(id)
    if not prod:
        return None, f"Product {id} not found"
    db.remove(prod)
    return True,None