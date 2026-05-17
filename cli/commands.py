import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.inventory_service import (
    add_product, get_all,get_one, update_product, delete_product
)
from app.services.off_service import search_product
def search(id):
    prod=search_product(id)
    print(prod if prod else "Product not found")
def add(id,price,stock):
    prod,err=add_product(id,float(price),int(stock))
    print(err if err else f"Added: {prod}")
    pass
def update(id,price=None,stock=None):
    print(update_product(
        id,
        float(price) if price else None,
        int(stock) if stock else None
    ))
def view():
    prod=get_all()
    for p in prod:
        print(p)

def view_one(id):
    prod=get_one(id)
    print(prod if prod else f"Product {id} not found")

def delete(id):
    _,err=delete_product(id)
    print(err if err else f"Deleted product {id}")

def main():
    args=sys.argv[1:]
    if not args:
        print("Usage: python commands.py <command> [args]")
        return
    cmd=args[0]
    match cmd.lower():
        case "search" if len(args)==2:
            search(args[1])
            
        case "add" if len(args)==4:
            add(args[1],args[2],args[3])
                    
        case "view" if len(args)==1:
            view()
            
        case "view" if len(args)==2:
            view_one()
            
        case "update" if len(args)>=3:
            price=args[2] if len(args)>2 else None
            stock=args[3] if len(args)>3 else None
            update(args[1],price,stock)
            
        case "delete" if len(args)==2:
            delete(args[1])
            
        case _:
            print("Commands:")
            print("  search <barcode>")
            print("  add <barcode> <price> <stock>")
            print("  view")
            print("  update <barcode> <price> <stock>")
            print("  delete <barcode>")

if __name__ == "__main__":
    main()