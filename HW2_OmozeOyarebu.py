"""
Omoze Oyarebu
CS 100 2023S Section 012
HW 02, February 11, 2023

"""

#Exercise 1
#1a
a = 3
b = 4
c = 5

#1b
if a < b:
    print("OK")

#1c
if c < b:
    print("OK")

#1d
if (a + b == c):
    print("OK")

#1e
if (pow(a,2) + pow(b,2) == pow(c,2)): #pow is a built in math function that raises a number to a specified power(number, raised to desired power)
    print("OK")
print()

#Exercise 2
if a < b:
    print("OK")
else:
    print("NOT OK")

#1c
if c < b:
    print("OK")
else:
    print("NOT OK")

#1d
if (a + b == c):
    print("OK")
else:
    print("NOT OK")

#1e
if (pow(a,2) + pow(b,2) == pow(c,2)): #pow is a built in math function that raises a number to a specified power(number, raised to desired power)
    print("OK")
else:
    print("NOT OK")
print()

#Exercise 3
grades = ['A','B','C','D','C','A','B','F','F','F']
letter = ['A', 'B', 'C', 'D', 'F']
frequency = []
for x in letter:
    frequency = [grades.count(x)]
    print(x,'=',frequency)

#Exercise4
#4a
dog_breeds = ['collie', 'sheepdog','chow','chihuahua']
print('dog breeds =',dog_breeds)   

#4b
herding_dogs = dog_breeds[0:2] #sliced list
print('herding dogs =',herding_dogs)

#4c
tiny_dogs = dog_breeds[-1] #using negative indexing to access last element
print('The last item is:',tiny_dogs)

#4d
character_serach = 'persian'
if (character_serach in dog_breeds):
    print('True')
else:
    print('False')