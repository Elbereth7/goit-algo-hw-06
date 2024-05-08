from collections import UserDict
from record import Record

# Class for storing and managing records.
class AddressBook(UserDict):
    # Add record to self.data
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    # finds a record by name
    def find(self, name):
        if name in self.data.keys():
            return self.data[name]

    # deletes a record by name
    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
    