
class jedi(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def JediNameConstructor(self):
        part1 = self.firstname[:2]
        part2 = self.lastname[:3]
        name = part2 + part1
        return name
        
      
myJedi = jedi("wil", "damato")
print(dir(myJedi))
print(myJedi.JediNameConstructor())