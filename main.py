from address_book import AddressBook
from record import Record

if __name__ == '__main__':
    # Creating a new address book
    book = AddressBook()

    # Creating a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Adding John record to the address book
    book.add_record(john_record)

    # Creating and adding new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Displaying all records in the book
    for name, record in book.data.items():
        print(record)

    # Finding and editing John's phone number
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Result: Contact name: John, phones: 1112223333; 5555555555

    # Looking for a specific phone number in John record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    # Removing Jane record
    book.delete("Jane")

    # Displaying all records in the book
    for name, record in book.data.items():
        print(record)

    # Creating and adding new record for Maciej
    maciej_record = Record("Maciej")
    maciej_record.add_phone("2039459284")
    book.add_record(maciej_record)
    maciej_record.add_phone("7779459284")
    maciej_record.add_phone("5745469284")

    # Displaying all records in the book
    for name, record in book.data.items():
        print(record)

    # Removing Maciej's phone
    maciej_record.remove_phone('2039459284')

    # Displaying all records in the book
    for name, record in book.data.items():
        print(record)

    # Trying to remove, edit and find nonexisting phone
    # maciej_record.remove_phone('5230949014')
    # maciej_record.edit_phone('5230949014', '8594055344')
    # maciej_record.find_phone('5230949014')

