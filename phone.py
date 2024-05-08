from field import Field

# Class for storing the record phone
class Phone(Field):
    # Includes phone number validation (must be equal to 10)
    def __init__(self, value):
        super().__init__(value)
        assert len(value) == 10, f'Phone {value} length is not equal to 10 digits'