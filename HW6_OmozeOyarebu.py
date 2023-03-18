"""
Omoze Oyarebu
CS 100 2023S Section 012
HW 06, March 23, 2023

"""
#Problem 1
def twoWords(length:int,firstletter:str):
  word_list = []
  while True:
    print("Enter a ", length,"-letter word please: ")
    word = input()
    if (len(word) == length):
      word_list.append(word)
      break
    
  while True:
    print("Enter a word beginning with",firstletter,"please: ")
    word2 = input()
    if (word2[0] == firstletter) or (word2[0] == firstletter.swapcase()):
      word_list.append(word2)
      break 
  return word_list

twoWords(4,"b") #function call

#Problem 2
def twoWordsV2(length:int,firstletter:str):
  word_list = []
  
  while (length != 0):
    print("Enter a ", length,"-letter word please: ")
    word = input()
    if (length == len(word)):
        word_list.append(word)
        length = 0
    
    while (firstletter != '0'):
       print("Enter a word beginning with",firstletter," please: ")
       word2 = input()
       if (word2[0] == firstletter) or (word2[0] == firstletter.swapcase()):
          word_list.append(word2)
          firstletter = '0'   
  return word_list

twoWordsV2(4,'b') #function call

#Problem 3
def enterNewPassword():
    update = 0
    while (update != -1):
        password = str(input("Enter a password that has 8-15 characters and that contains at least one digit"))

        #inner function that checks whether a string contains digits
        def digit_Exists(str_num):
            for x in str_num:
                if (x in "0123456789"):
                    return True
                
                
        if (digit_Exists(password) == True) and ((len(password) < 8) or (len(password) > 15)):
            print("Try again. Enter a password with 8-15 characters")
        elif (digit_Exists(password) != True ) and ((len(password) < 8) or (len(password) > 15)):
            print("Try again. Enter a password with 8-15 characters with at least 1 digit")
        elif (digit_Exists(password) != True ) and ((len(password) >= 8) or (len(password) <= 15)):
            print("Try again. Enter password with at least one digit")
        else:
            print("Password is good.")
            update = -1

enterNewPassword() #function call

#Problem 4
def GuessNumber():
    import random
    num = random.randrange(0,51)

    trys = 1
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it")
    while (trys != 6):
        print("Guess",trys)
        guess = int(input())
        if (guess > num):
            print(guess,"is too high")
            trys += 1
        elif (guess < num):
            print(guess,"is too low")
            trys += 1
        elif (guess == num):
            print("You are right! I was thinking of",num,"!")
            trys = 6
        
        if (trys == 6) and (guess != num):
            print("Game Over.You've reached the maximum tries allowed")
      
GuessNumber() #function call