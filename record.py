from name import Name
from phone import Phone

# Class for storing contact information, including name and list of phone numbers
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    # Method for adding Phone objects
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Method for removing Phone objects
    def remove_phone(self, phone):
        if phone in [p.value for p in self.phones]:
            self.phones = [p for p in self.phones if p.value != phone]
        else:
            print(f"Removing phone {phone} failed. Phone {phone} not found for contact {self.name}")

    # Method for editing Phone objects
    def edit_phone(self, phone, new_phone):
        found = False
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone
                found = True
        if not found:
                print(f"Editing phone {phone} failed. Phone {phone} not found for contact {self.name}")
        
    # Method for finding Phone objects
    def find_phone(self, phone):
        if phone in [p.value for p in self.phones]:
            return Phone(phone)
        else:
            print(f"Finding phone {phone} failed. Phone {phone} not found for contact {self.name}")
            return None