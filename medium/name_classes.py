class Name:

    def __init__(self, fname, lname):
        self.fname = fname.title()
        self.lname = lname.title()
        self.fullname = "{} {}".format(self.fname, self.lname)
        self.initials = "{}.{}".format(self.fname[0], self.lname[0])
