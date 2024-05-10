from field import Field

# Class for storing the record phone
class Phone(Field):
    # Includes phone number validation (must be equal to 10 numbers)
    def __init__(self, value):
        super().__init__(value)
        if len(self.value) != 10 or self.value.isnumeric() == False:
            raise ValueError(f'Phone {self.value} format is incorrect: phone must consist of 10 numbers')

        
