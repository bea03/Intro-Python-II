# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description)
        #needs a name
        self.name = name
        #needs a description
        self.description = description
        #needs connected rooms, default is set to none.
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

