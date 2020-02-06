from time import *
roomArray = []
itemArray = []
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
roomArray[503] = ""
roomArray[504] = ""
roomArray[505] = ""
roomArray[506] = ""
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

def main():
    location = 506
    print("jukgtf")
    print("by Kye, Yasmine, Miri, Kyle")
    sleep(1)
    while True:
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
        print(str(roomArray[location]))
        if location == 805:
            print("do you want to pick up LegoBot? n or y?")
            answer = input()
            if answer == "y":
                inventoryArray.append("LegoBot")
        if location == 704:
            print("do you want to pick up the Keyboard? y or n?")
            answer = input()
            if answer == "y":
                inventoryArray.append("Keyboard")
        if location == 503:
            print("do you want to pick up the iPad? y or n?")
            answer = input()
            if answer == "y":
                inventoryArray.append("iPad")
        if location == 505:
            print("do you want to pick up the poster? y or n?")
            answer = input()
            if answer == "y":
                inventoryArray.append("poster")
        if location == 303:
            print("do you want to pick up the Baguette? y or n?")
            answer = input()
            if answer == "y":
                inventoryArray.append("Baguette")
        if location == 203:
            print("do you want to pick up the Eiffel Tower? y or n?")
            answer = input()
            if answer == "y":
                inventoryArray.append("Eiffel Tower")
        if location == 204:
            print("do you want to pick up the Beret? y or n?")
            answer = input()
            if answer == "y":
                inventoryArray.append("Beret")
        if location == 304:
            print("do you want to pick up the Bidet? y or n?")
            answer = input()
            if answer == "y":
                inventoryArray.append("Bidet")
        if location == 306:
            print("do you want to pick up the Wrench? y or n?")
            answer = input()
            if answer == "y":
                inventoryArray.append("Wrench")
        if location == 307:
            print("do you want to pick up the Robot Arm? y or n?")
            answer = input()
            if answer == "y":
                inventoryArray.append("Robot Arm")
        userInput = input("Please type: n, s, e, w, or quit: ")
        location = move(userInput, location)

