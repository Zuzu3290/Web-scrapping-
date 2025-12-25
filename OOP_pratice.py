class Human:
    #method is just a function conatined in a class

    def __init__(self, name , gender):  # the stupid way of having a constrcutor 
        self.name = name
        self.gender = gender 

        #So no destructor lol and only one constructor so no overloading but we have default parameters  
          
    def baby(self):
        print("waaa waa waaa")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.gender}.")

people1 = Human("Hello", "Male")  #object instantiation
print(people1.greet())  #method calling