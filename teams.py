from time import *
from map import *
from random import *

roomArray = []
itemArray = []
inventoryArray = []
for i in range(999):
    roomArray.append(False)
    itemArray.append(False)
#French room
roomArray[203] = "You walked toward the steel structure, and now you're standing under a mini eiffel tower that really isn't that small. South you see a Beret, near an oven. Back east, the table you saw walking in is still there. North and South you're blocked off by walls."
roomArray[303] = "As you walk into the room, you see a table with a freshly cooked Baguette on it. LOoking south, you see a toilet..? There is a wall up north, the hallway you entered in is south, west you get a closer view of the steel structure, and you see the Eiffel Tower!"
roomArray[204] = "The oven looks like another Baguette is being cooked in it. There is a beret beside it, on a cutting board. North is the eiffel tower, east is a toilet, with no toilet paper.. Weird.. South and west are walls."
roomArray[304] = "You walk towards the toilet, and notice a weird detachable contraption on the toilet. It says 'Bidet'? Looks useful. North is the table from the entrance, west is the oven. East and south are blocked off by walls."
roomArray[403] = "From the hallway, you walk into the French room. You can only go forward, as there's a short hallway into the room. You see a Baguette to your west, and a huge steel structure farther west?"

#Hallway
roomArray[503] = "you find an ipad on the floor. to your east is another anime club poster. to your west is the french classroom."
roomArray[504] = "You find a a pair of headphones on the ground. To be honest, if I were you, I wouldn't trust them. They look kinda crusty. To your east is the computer lab."
roomArray[505] = "To the east is a wall with another anime club poster."
roomArray[506] = "You've entered the hallway. To your north and south are endless halls of doom. To the east is a wall with an anime club poster and to your west is the engineering room."
#Computer lab
roomArray[604] = "You're entering the computer lab. You see a computer to your east, there are walls to your north and south."
roomArray[704] = "You see a computer. It looks like the person left some coding on the screen, there is a wall to your north."
roomArray[804] = "You wander in the computer lab. You can see some sort of robot to the south, there are walls to the north and east."
roomArray[705] = "You are walking inside of the computer lab. You see some sort of robot to the east, there are walls to the south and west."
roomArray[805] = "You are in the computer lab and see a LegoBot. Something about the LegoBot seems off, there are walls to the east and south."
#Engineering room
roomArray[206] = "you are in the corner of the engineering room, to the east you see a cabinet and walls are to the north and west."
roomArray[306] = "you open a big cabinet and find a metal wrench to the south you see a table with something metallic on it and a wall to the north"
roomArray[406] = "to the east is the door to the hallway and to the west is a closed cabinet and walls are to the north snd south"
roomArray[207] = "to the east you see something metallic on a table and walls to the west and south"
roomArray[307] = "you find what appears to be a metal arm on a table, to the north you see a cabinet and you see walls to the east and south"
#Secret Room
roomArray[309] = "you are in an enclosed room, you have seemed to teleport, there are walls to your north and east."
roomArray[209] = "you are wandering in the enclosed room, there are walls to your north and west."
roomArray[210] = "You are wandering in an enclosed room, there are walls to your south and west."
roomArray[310] = "You are wandering in an enclosed room, there are walls to your south and east."
def doesRoomExist(roomNumber):
    try:
        if roomArray[roomNumber] == False:
            print("You can’t go there")
            return False
        else:
            return True
    except:
        print("You can’t go there")
        return False
    
def move(userInput, location):
    if userInput == "n" and doesRoomExist(location - 1) == True:
        location -= 1 
    elif userInput == "s"and doesRoomExist(location + 1) == True:
        location += 1
    elif userInput == "e"and doesRoomExist(location + 100) == True:
        location += 100
    elif userInput == "w"and doesRoomExist(location - 100) == True:
        location -= 100
    return location
def robotQuizGame():
    print("Hello. You are now trapped to play my game. Guess a number 1 through 5, and if you are right you'll be free.")
    randomNumber = randint(1, 5)
    input1 = input()
    while True:
            print("Guess a number")
            input1 = input()
            input1 = int(input1)
            if input1 < randomNumber:
                print("The secret word is after" + str(input1))
            if input1 > randomNumber:
                print("The secret word is before" + str(input1))
            if input1 == randomNumber:
                print("You got it!!!!!")
                print("Do you want to play again? y or n?")
                input2 = input()
                if input2 == "y" :
                    robotQuizGame()
                if input2 == "n" :
                    print("You can continue")
                    quizCompleted = True
                    break
def specialRooms():
    global location, quizCompleted, bossDead
    if location == 809 and quizCompleted == False:
        robotQuizGame()
def main():
    map = Map()
    location = 506
    print("   __                                         __ ")                
    print("  /  )           _/_                    /    /  )      /   _/_  ") 
    print(" /--<  _  __  _  /  _     __.  ____  __/    /--<  o __/ _  /  _  ")
    print("/___/_</_/ (_</_<__/_)_  (_/|_/ / <_(_/_   /___/_<_(_/_</_<__/_)_")
    print("by Kye, Yasmine, Miri, Kyle")
    
    sleep(1)
    inventoryArray = []
    itemArray[805] = "LegoBot"
    itemArray[704] = "Keyboard"
    itemArray[503] = "iPad"
    itemArray[505] = "Poster"
    itemArray[303] = "Baguette"
    itemArray[203] = "Eiffel Tower"
    itemArray[204] = "Beret"
    itemArray[304] = "Bidet"
    itemArray[306] = "Wrench"
    itemArray[307] = "Robot Arm"
    itemArray[209] = "Gold Key"

    while True:
        map.draw(roomArray, itemArray, location)
        print(roomArray[location])
        specialRooms()
        if itemArray[location] != False:
            print("items in room: " + itemArray[location])
            userInput = input("Please type: n, s, e, w, take, or quit: ")
            if userInput == "take":
                inventoryArray.append(itemArray[location])
                itemArray[location] = False
        else:
            userInput = input("Please type: n, s, e, w, or quit: ")
        if userInput == "quit":
            print("thank you")
            break
        
        location = move(userInput, location)
