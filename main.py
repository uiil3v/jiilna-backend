products = []

num_products = int(input("Enter the number of products: "))

for item in range(num_products):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    
    total = quantity * price
    tax = total * 0.15
    final_total = total + tax
    
    print()
    print("----------------------")
    print(f"Product: {name}")
    print(f"Total: {total}")
    print(f"Tax: {tax}")
    print(f"Final Total: {final_total}")
    print()
    
    product = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "total": total,
        "tax": tax,
        "final_total": final_total
    }

    products.append(product)
    

print("----------------------")
for product in products:
    print(product)