import datetime

class Contacts:
    def __init__(self, name, phone_number, address, birthday):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.birthday = birthday

    def __repr__(self):
        print('Welcome to my contacts application')
        return 'Name : ' + self.name + ', phone number: ' + self.phone_number + ', address: ' + self.address + ' and birthday: ' + self.birthday

    
# Instances (contacts):
john_appleseed = Contacts('John Appleseed', 07895446782, '21 Ellison Road', datetime.date(1968, 07, 15))

# Testing
print(john_appleseed)