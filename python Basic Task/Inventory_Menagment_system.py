inventory = {}

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price": float(price), "stock": int(stock)}
        print(f"Item '{item}' added successfully.")

def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
        return

    new_stock = inventory[item]["stock"] + quantity

    if new_stock < 0:
        print(f"Error: Insufficient stock for '{item}'.")
    else:
        inventory[item]["stock"] = new_stock
        print(f"Stock for '{item}' updated successfully.")

def check_availability(item):
    if item not in inventory:
        return "Item not found"
    else:
        return inventory[item]["stock"]

# Naya sales_report function
def sales_report(sales):
    total_revenue = 0.0

    for item, quantity_sold in sales.items():
        # 1. Check: Kya item inventory mein hai?
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue

        # 2. Check: Kya kafi stock hai?
        if inventory[item]["stock"] < quantity_sold:
            print(f"Error: Insufficient stock for '{item}'.")
            continue

        # 3. Revenue hisab karna aur stock kam karna
        price = inventory[item]["price"]
        total_revenue += quantity_sold * price
        inventory[item]["stock"] -= quantity_sold

    # 4. Formatted revenue string return karna
    return f"Total revenue: ${total_revenue:.2f}"

# Bottom testing block:
add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange error print karega
print(sales_report(sales))  # Output: Total revenue: $19.00
print(inventory)