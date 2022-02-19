class Node(object):
    def __init__(self, id):
        self.id = id 
    
    def get_id(self):
        return self.id
    
    def __str__(self):
        return f"{self.id}"
    
    def __repr__(self):
        return self.__str__()
    
    