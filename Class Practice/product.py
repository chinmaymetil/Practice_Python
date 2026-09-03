products = {
    1: "Laptop",
    2: "Mobile",
    3: "Headphones",
    4: "Keyboard"
}

def show_products():
    print("Amazon Products:")
    for id, name in products.items():
        print(id, name)

def buy_product(id):
    if id in products:
        print("You bought:", products[id])
    else:
        print("Product not found")