"""
Omoze Oyarebu
CS 100 2023S Section 012
HW 10, April 28, 2023

"""

class Dog:

    """ Represents festures of a dog """

    Species = " Canis familiaris" #Species of domestic dogs

    def __init__(self, name,breed):
        self.Name = name 
        self.Breed = breed

        """ problem 2- adding Tricks """
        self.Tricks = [] 
       

    """ Problem 3-teach method """
    def teach(self,string):
        self.Tricks.append(string)
        print("{} knows {}".format(self.Name, ",".join(self.Tricks)))

    """ problem 4 """
    def knows(self,check_tricks):
        self.check = check_tricks

        if (check_tricks in self.Tricks):
            print("Yes,",self.Name,"knows",self.check)
        else:
            print("No,",self.Name,"doesn't know",self.check)
        
#client program that uses the Dog class
def main():
    sugar = Dog("Sugar","Border Collie")
    print("This dog's name is",sugar.Name)
    print("It is a",sugar.Breed,"\n")

    #creating a second dog
    cody = Dog("Cody","German Shepherd")
    print("This dog's name is",cody.Name)
    print("It is a",cody.Breed,"\n")


    #problem 2
    print(sugar.Tricks,"\n")
    print(cody.Tricks,"\n")

    #problem 3
    cody.teach("frisbee")
    sugar.teach("Hoop Jump\n")

    #print(cody.Tricks)
    #print(sugar.Tricks,"\n")
    
    #problem 4
    cody.knows("frisbee")
    sugar.knows("Hoop Jump\n")
    

    #problem 5
    print(sugar.Name,"belongs to the dog species of",sugar.Species)
    print(cody.Name,"belongs to the dog species of",cody.Species)

#ensures that main() is only called within this script
if __name__ == '__main__':
    main()

