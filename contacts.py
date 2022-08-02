class Contacts:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    @property
    def information(self):
        return f"""
        Name : {self.name}
        Phone Number : {self.phone_number}
        Email : {self.email}
        """

