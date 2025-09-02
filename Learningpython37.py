class car:
    
    def __init__ (self,a , b, c):
        self.engine = a
        self.cc = b
        self.type = c
        
    def kit(self):
        print(f"The car engine is {self.engine}and the cc is {self.cc}the type is {self.type}")
            
            
aulto = car("petrol",100,"manual")
suzuki =car("petrol",101,"automatic")

print(aulto.engine)
print(suzuki.type)
aulto.kit()
            
            
            
            
            # This CONCEPT IS CLASS