class Person:
    Age = 0

    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.Age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        #print("Age ", self.Age, end="\n")
        if (self.Age<0):
            print("Age is not valid, setting age to 0.")
            self.Age = 0
        if (self.Age < 13):
            print("You are young.")
        elif self.Age >= 13 and self.Age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")


    def yearPasses(self):
        # Increment the age of the person in here
        self.Age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")