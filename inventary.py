

# List to store product names
products = []

# Tuple to store product categories (fixed values)
categories = ("Electronics", "Clothing", "Food", "Stationery")

# Set to store unique suppliers
suppliers = set()

# Dictionary to store product and quantity
inventory = {}


def add_product():
    """
    Add a new product to the inventory.
    """
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    supplier = input("Enter supplier name: ")

    products.append(name)
    suppliers.add(supplier)
    inventory[name] = quantity

    print("Product added successfully.")


def view_products():
    """
    Display all products in the inventory.
    """
    if len(products) == 0:
        print("No products in inventory.")
    else:
        print("Products List:")
        for p in products:
            print(p)


def view_inventory():
    """
    Display products with their quantities.
    """
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Inventory Details:")
        for product, qty in inventory.items():
            print(product, ":", qty)


def view_suppliers():
    """
    Display unique suppliers.
    """
    print("Suppliers List:")
    for s in suppliers:
        print(s)


def view_categories():
    """
    Display product categories (Tuple example).
    """
    print("Available Categories:")
    for c in categories:
        print(c)


def menu():
    """
    Display the menu options.
    """
    print("\nInventory System")
    print("1. Add Product")
    print("2. View Products")
    print("3. View Inventory")
    print("4. View Suppliers")
    print("5. View Categories")
    print("6. Exit")


# Main program loop
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        view_inventory()

    elif choice == "4":
        view_suppliers()

    elif choice == "5":
        view_categories()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")