# Store Items List

items = []

while True:
    print("STORE MENU")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add Item
    if choice == "1":
        item = input("Enter item name: ")
        items.append(item)
        print("Item added successfully. ")

    # Remove Item
    elif choice == "2":
        if len(items) == 0:
            print("No items to remove")
        else:
            print("Items in store:")
            i = 0
            for x in items:
                print(i + 1, "-" , x)
                i = i + 1

            num = int(input("Enter item number to remove: "))
            if num > 0 and num <= len(items):
                removed_item = items.pop(num - 1)
                print(removed_item, "removed successfully.")
            else:
                print("Invalid number.")

    # View Items
    elif choice == "3":
        if len(items) == 0:
            print("List is empty.")
        else:
            print("Store Items:")
            i = 1
            for x in items:
                print(i, x)
                i = i + 1



    # Exit
    elif choice == "4":
        print("Thanks for coming ! Goodbye!")
        break

    else:
        print("Wrong choice , try again.")