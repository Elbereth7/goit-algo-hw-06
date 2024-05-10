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
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    # Method for removing Phone objects
    def remove_phone(self, phone):
        if phone in [p.value for p in self.phones]:
            self.phones = [p for p in self.phones if p.value != phone]
        else:
            raise ValueError (f"Removing phone {phone} failed. Phone {phone} not found for contact {self.name}")

    # Method for editing Phone objects
    def edit_phone(self, phone, new_phone):
        old_phone = self.find_phone(phone)
        if not old_phone:
            raise ValueError (f"Editing phone {phone} failed. Phone {phone} not found for contact {self.name}")
        self.add_phone(new_phone)
        self.remove_phone(phone)
            
        
    # Method for finding Phone objects
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        else:
            raise ValueError (f"Finding phone {phone} failed. Phone {phone} not found for contact {self.name}")