#By Ausar Square - Musa
import time
import os
groceryList={ "apple":0.99 , "banana":1.50, "eggs":3.99 , "waffles":2.69, "bacon":6.99, "milk":4.59, "chicken wings":12.89, "donuts":0.69, "beans":1.99, "rice":3.49}
                        

def menu():
    print ("  ")
    print ("Welcome to Your Grocery List Helper")
    print ("1 - Add a Food")
    print ("2 - Delete a Food")
    print ("3 - List The Foods")
    print ("4 - Lookup a Food")
    print ("5 - Exit")
    print ("  ")

def cls():
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
          


def getPrice(item):
    return groceryList[item]
    
        
        
KeepGoing = True
myList=[]
totalPrice = 0
count=0
size=len(myList)
print "There are " , size , " items in the List"
while KeepGoing:
    cls()
    menu()
    ans = input("Enter A Value ")

    if ans==1:
         # Adds an item in the list
        b=raw_input("What item would you like to add: ")
        b.strip()
        myList.append(b)
        price = getPrice(b)
        print "The price of a ", b , "is", price
        totalPrice = totalPrice + price
        print "Your total cost of all foods is: $", + totalPrice
        
        
       
    if ans==2:
        # Checks off an item in the list
        c=raw_input("What item would you like to delete/check off: ")
        myList.remove(c)
        
    if ans==3:
        #  Prints the list (to check your work)
        print ("  ")
        print ("The list so far has: "+"\n")
        for everyItem in myList:
            print ("  " + everyItem)
    if ans==4:
         # Finds item in the list
         
         item=raw_input('What item would you like to find ')
         if item in myList:
             print item ," is in my grocery list"
             item_count = 0
             for el in myList:
                 if el == item:
                     item_count = item_count + 1

             cost = item_count * groceryList[item]
             
             print ("You have " + str(item_count) + " " + item + " in your list. This will cost $" + str(cost))
                         
         else:
             print item, "is not in my grocery list"
             myList.index(item)
             
    if ans==5:
         # The Exit Door
         if len(myList) > 0:
             print ("You forgot to get " + str(myList))
         print ("     Thank you, Goodbye")
         KeepGoing=False




