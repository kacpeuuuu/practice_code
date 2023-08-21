class Person():
    def __init__(self, first_name, last_name, age, height, weight, hometown):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age 
        self.height     = height
        self.weight     = weight
        self.hometown   = hometown

    def walking(self):
        #print(f'{first_name} is walking') / NAME ERROR FIX -> self.first_name
        print(f'{self.first_name} is walking')

    def stop_walking(self):
        #print(f'{first_name} has stopped walking')
        print(f'{self.first_name} has stopped walking')



David = Person("David", "Smith", 27, 195, 105, "Compton")


print(David.first_name)
print(David.last_name)
print(David.age)
print(David.height)
#print(David.walking())         THIS STATEMENT ALREADY HAS PRINT SO PRINT 2X IS USELESS
#print(David.stop_walking())        ^^^^^^^

David.walking()
David.stop_walking()
