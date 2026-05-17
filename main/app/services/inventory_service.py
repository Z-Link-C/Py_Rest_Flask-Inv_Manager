from .off_service import search_product
def add_product(code,price,stock):
    prod_data=search_product(code)
    if not prod_data: return None, "Product not found in Database."
    
def get_all():
    pass
def update_product(code,price=None,stock=None):
    pass
def delete_product(code):
    pass