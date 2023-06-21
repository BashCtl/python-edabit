class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = "{} {}".format(firstname, lastname)
        self.email = "{}.{}@company.com".format(firstname.lower(), lastname.lower())
    # Complete the code!
