# For customer inputing
customers = {}   

# Circle for user to choose until they choose to exit
while True:      
    print("1. Add  2. Search  3. Delete  0. Exit")
    choice = input("Please choose: ").strip()

    if choice == "1":
        name  = input("Name: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone: ").strip()

# Only add if all three fields are not empty
        if name and email and phone:          
            customers["C001"] = {"name": name, "email": email, "phone": phone}
            print("Added successfully!")
        else:
            print("Incomplete information, please try again.")

    elif choice == "2":
        kw = input("Please enter the name keyword: ").strip()
        for cid, info in customers.items():
            if kw in info["name"]:
                print(cid, info)

    elif choice == "3":
        cid = input("Please enter the ID of the customer to delete: ").strip()
        if cid in customers:
            del customers[cid]
            print("Deleted successfully!")
        else:
            print("Customer not found.")

    elif choice == "0":
        print("Goodbye!")
        break   