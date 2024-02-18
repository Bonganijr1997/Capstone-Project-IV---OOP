from tabulate import tabulate

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Code: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}"


shoes_list = []

def read_shoes_data():
    """
    Read shoe data from the file 'inventory.txt' and populate the shoes_list.

    Returns:
    None
    """
    try:
        with open("inventory.txt", "r") as file:
            header = next(file)  # Read and skip the header line
            for line in file:
                data = line.strip().split(",")
                country, code, product, cost, quantity = data
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoes_list.append(shoe)
        print("Shoe data loaded successfully.")
    except FileNotFoundError:
        print("File 'inventory.txt' not found.")

def capture_shoes():
    """
    Capture shoe details from the user and add a new shoe to the shoes_list.

    Returns:
    None
    """
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    print("Shoe added successfully.")

def view_all():
    """
    View details of all shoes in the shoes_list.

    Returns:
    None
    """
    table = []
    for shoe in shoes_list:
        table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate(table, headers=headers))

def re_stock():
    """
    Find and restock the shoe object with the lowest quantity.

    Returns:
    None
    """
    if not shoes_list:
        print("No shoes available.")
        return

    lowest_quantity_shoe = min(shoes_list, key=lambda shoe: shoe.quantity)
    print(f"Shoe with the lowest quantity:\n{lowest_quantity_shoe}")

    choice = input("Do you want to restock this shoe? (yes/no): ")
    if choice.lower() == "yes":
        quantity = int(input("Enter the quantity to be added: "))
        lowest_quantity_shoe.quantity += quantity
        print("Shoe restocked successfully.")

def search_shoe():
    """
    Search for a shoe object by code and print its details.

    Returns:
    None
    """
    code = input("Enter the shoe code: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print(f"Shoe found:\n{shoe}")
            return
    print("Shoe not found.")

def value_per_item():
    """
    Calculate and print the total value for each shoe item.

    Returns:
    None
    """
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"Product: {shoe.product}\nTotal Value: {value}")

def highest_qty():
    """
    Print the shoe object with the highest quantity available for sale.

    Returns:
    None
    """
    if not shoes_list:
        print("No shoes available.")
        return

    highest_quantity_shoe = max(shoes_list, key=lambda shoe: shoe.quantity)
    print(f"Highest quantity shoe for sale:\n{highest_quantity_shoe}")

# Main menu
while True:
    print("\n=== Shoe Inventory Management ===")
    print("1. Load Shoe Data from File")
    print("2. Capture Shoe")
    print("3. View All Shoes")
    print("4. Restock Shoes")
    print("5. Search Shoe")
    print("6. Value per Item")
    print("7. Highest Quantity Shoe")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")