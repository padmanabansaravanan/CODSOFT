class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Contact {name} added successfully!")

    def update_contact(self, name, number):
        if name in self.contacts:
            self.contacts[name] = number
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}, Number: {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")

    def display_contacts(self):
        print("Contacts:")
        for name, number in self.contacts.items():
            print(f"Name: {name}, Number: {number}")

# Example Usage
contact_book = ContactBook()
contact_book.add_contact("Alice", "1234567890")
contact_book.add_contact("Bob", "9876543210")
contact_book.display_contacts()
contact_book.update_contact("Alice", "9999999999")
contact_book.delete_contact("Bob")
contact_book.search_contact("Alice")
contact_book.search_contact("Bob")
