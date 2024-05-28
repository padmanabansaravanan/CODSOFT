todo_list = []
def display_list():
    if todo_list:
        print("To-Do List:")
        for index, item in enumerate(todo_list, 1):
            print(f"{index}. {item}")
    else:
        print("Your to-do list is empty.")

def add_item(item):
    todo_list.append(item)
    print(f"Added '{item}' to your to-do list.")

def remove_item(item_index):
    if item_index > 0 and item_index <= len(todo_list):
        removed_item = todo_list.pop(item_index - 1)
        print(f"Removed '{removed_item}' from your to-do list.")
    else:
        print("Invalid item index.")

while True:
    print("\n1. Display To-Do List\n2. Add Item\n3. Remove Item\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_list()
    elif choice == '2':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '3':
        item_index = int(input("Enter the index of the item to remove: "))
        remove_item(item_index)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the to-do list app!")
