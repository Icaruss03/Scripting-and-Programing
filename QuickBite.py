# QuickBite Food Ordering System Prototype

# Menu data structure using nested dictionaries and lists
menu = {
    "Appetizers": [
        {"item": "Spring Rolls", "price": 5.00},
        {"item": "Garlic Bread", "price": 3.50}
    ],
    "Main Course": [
        {"item": "Margherita Pizza", "price": 10.00},
        {"item": "Pasta Alfredo", "price": 8.50}
    ],
    "Desserts": [
        {"item": "Cheesecake", "price": 6.00},
        {"item": "Brownie", "price": 4.50}
    ],
    "Beverages": [
        {"item": "Coke", "price": 1.50},
        {"item": "Orange Juice", "price": 2.00}
    ]
}

# Initialize an empty order list
order = []


# Display the menu
def display_menu():
    print("\nQuickBite Menu:\n" + "=" * 20)
    for category, items in menu.items():
        print(f"\n{category}:")
        for item in items:
            print(f"{item['item']} - ${item['price']:.2f}")


# Add item to the order
def add_to_order(item_name):
    for category, items in menu.items():
        for item in items:
            if item["item"].lower() == item_name.lower():
                order.append(item)
                print(f"Added {item['item']} - ${item['price']:.2f} to your order.")
                return
    print("Item not found in menu. Please check your spelling and try again.")


# Function to delete an item from the order
def remove_from_order():
    # Display the current order
    print("\nThis is your current order:\n")
    display_order()
    choice = input("\nWould you like to delete an item?\n1. Yes\n2. No\n")

    if choice == "1":
        # If user wants to delete an item
        print("\nWhich item would you like to remove?\n")

        # Iterate through the list of items, numbering them
        i = 1
        for item in order:
            print(f"\n{i}. {item['item']} - {item['price']:.2f}\n")
            i = i + 1

        while True:

            # Ask the user to select which item they want to delete
            item_index = input("\nEnter the number of the item you want to remove:\n")
            # Subtract 1 to get the actual index of the item in the list
            # (when we number items for the user we start with 1, while list indices start from 0)
            item_index = int(item_index) - 1

            # Delete the exact item at item_index, keeping data consistency
            # The order.remove(order[item_index]) would have removed the first occurrence of that given item, not the exact copy we want
            if item_index > len(order) - 1:
                print(f"Not a valid option")
            else:
                del order[item_index]
                break
    else:
        # If user does not want to delete an item, exit the function
        return


# Calculate total cost of the order
def calculate_total():
    total = sum(item["price"] for item in order)
    return total


# Display order summary and total
def display_order():
    if not order:
        print("\nYour order is currently empty.")
        return
    print("\nYour Order Summary:\n" + "=" * 20)
    for item in order:
        print(f"{item['item']} - ${item['price']:.2f}")
    print(f"\nTotal Amount: ${calculate_total():.2f}")


# Main ordering loop
def place_order():
    while True:
        # Moved display_menu() here in order to display the menu each time the user has to make a choice
        display_menu()
        choice = input(
            "\nEnter an item to add to your order.\n1. View order using 'view'\n2. Delete an item from your order using 'delete'\n(or type 'done' to finish): ")

        # Added options to view current order and to access the delete menu
        if choice == "view":
            display_order()
            choice2 = input("\nWould you like to checkout?\n1. Yes\n2. No\n")
            if choice2 == "1":
                break
            elif choice2 == "2":
                display_menu()
                continue
        elif choice == "delete":
            remove_from_order()
        elif choice.lower() == 'done':
            break
        else:
            add_to_order(choice)


# Show order, calculate and display total bill
def checkout():
    print("\nChecking Out...\n" + "=" * 20)
    display_order()
    total = calculate_total()
    print(f"\nThank you for ordering! Your total bill is ${total:.2f}\n")


# Run the QuickBite ordering system
def run_quickbite():
    print("\nWelcome to QuickBite!\n" + "=" * 20)
    choice = input("\nPlease choose an option (write 'exit' otherwise):\n" + "=" * 20 + "\n1. Eat in\n2. Takeaway\n")
    if choice == "1":
        place_order()
    elif choice == "2":
        place_order()
    elif choice == "exit":
        return
    else:
        print("\nThis is not a valid option.\nPlease try again.\n\n" + "~" * 40)
        run_quickbite()

    checkout()


# Call the main function to start the program
run_quickbite()
