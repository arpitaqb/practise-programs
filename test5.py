#create a contect list using dictionary store name, phoneno. and emails.1.add 2.view 3.update 4.search 5.delete
contectlist = {}


def add_contect():
    name = input("Enter name of the person:__")
    phone = int(input(f"Enter phone no. of {name}:_"))
    email = input(f"Enter email adress of {name}:_")
    contectlist[name] = {f'phone': {phone}, 'email': {email}}
    print(f"contect {name} succesfully added into contactlist.")
    

def view_contect():
    if contectlist:
        print("Here is all contects in your list.")
        for i in contectlist:
            print(i)
    else:
        print("your contectlist is empty.")

def update_contect():
    name = input("Enter name of the person you want to update details:_")
    if name in contectlist:
        phone = input("Enter number :")
        email = input("Enter email:")
        if phone:
            contectlist[name]['phone'] = phone
        if email:
            contectlist[name]['email'] = email
        print(f"contact {name} updated sucessfully.")
    else:
        print(f"contact {name} not found.")

def search_contect():
    name = input("Enter name of the person you want to search:_")
    if name in contectlist:
        print(f"Name: {name}")
        print(f"phone no.: {contectlist[name]['phone']}")
        print(f"email: {contectlist[name]['email']}")
    else:
        print(f"{name} is not in the contect list.")

def delete_contect():
    name = input("enter name of the person you want to delete from your contectlist:_")
    if name in contectlist:
        del contectlist[name]
        print(f"{name} deleted from your contectlist.")
    else:
        print(f"there is no contect {name} in your contectlist.")

def main():
    while True:
        

        try:
            choice = int(input("Enter your choice........"))
        except ValueError:
            print("Enter a valid choice.")
            continue

        if choice == 1:
            view_contect()
        elif choice == 2:
            add_contect()
        elif choice == 3:
            update_contect()
        elif choice == 4: 
            search_contect()
        elif choice == 5:
            delete_contect()
        elif choice == 6:
            print("exiting the program.")
            break
        else:
            print("invalid choice. select from given numbers.")


if __name__ == "__main__":
    print()
    print("______________________Welcome to contectlist________________________________")
    print()
    print("What do you want to do?")
    print("Enter 1 to view your contect details.")
    print("Enter 2 to add new contect.")
    print("Enter 3 to update any existing contect.")
    print("Enter 4 to search any contect details.")
    print("Enter 5 to delete any existing contect.")
    print("Enter 6 to exit program.")
    main()
