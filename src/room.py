# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None)
        #needs a name
        self.name = name
        #needs a description
        self.description = description
        #needs connected rooms, default is set to none.
   '''  self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
'''
        self.connections = {
            "n": n_to
            "e": e_to
            "w": w_to
            "s": s_to
}
