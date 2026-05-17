import sys
from app.services.inventory_service import (
    add_product, get_all, update_product, delete_product
)
from app.services.off_service import search_product
def search(code):
    prod=search_product(code)
    print(prod if prod else "Product not found")
def add(code,price,stock):
    prod,err=add_product(code,float(price),int(stock))
    print(err if err else f"Added: {prod}")
    pass
def update(code,price=None,stock=None):
    print(update_product(
        code,
        float(price) if price else None,
        int(stock) if stock else None
    ))
def view():
    prod=get_all()
    for p in prod:
        print(p)
def delete(code):
    pass
def main():
    args=sys.argv[1:]
    if not args:
        print("Usage: python commands.py <command> [args]")
        return
    cmd=args[0]
    match cmd.lower():
        case "search" if len(args)==2:
            search(args[1])
            pass
        case "add" if len(args)==4:
            add(args[1],args[2],args[3])
            pass        
        case "view":
            view()
            pass
        case "update" if len(args)>=3:
            price=args[2] if len(args)>2 else None
            stock=args[3] if len(args)>3 else None
            update(args[1],price,stock)
            pass
        case "delete" if len(args)==2:
            delete(args[1])
            pass
        case _:
            print("Commands:")
            print("  search <barcode>")
            print("  add <barcode> <price> <stock>")
            print("  view")
            print("  update <barcode> <price> <stock>")
            print("  delete <barcode>")

if __name__ == "__main__":
    main()