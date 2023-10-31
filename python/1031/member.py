class Member:
    def __init__(self, member_id, name, age):
        self.member_id=member_id
        self.name=name 
        self.age=age
    
    def get_id(self):
        return self.member_id
    
    def get_name(self):
        return self.name 
    
    def get_age(self):
        return self.age