#created by Dimitri Franov

#Rooms
def room0():
    print("To the east you see a long dark corridor with a shimmering light at the end of it and to the west there is a staircase going down.")
    print("Use WASD to move")
    while True:
        b = input()
        if b != "w" and b !="a" and b !="s" and b !="d":
            print("No valid input")
        elif b=="w" or b =="s":
            print("You can't move in this direction")
        else:
            break
    if b=="d":
        print("You go along the corridor until you reach the end")
        room1()
    else:
        print("You go down a stairway carved out of stone, you open the old wooden door in front of you.")
        room2()

def room1():
    print("You stand in a square shaped room with a ceiling so high that the tall stone walls disappear into the darkness.")
    print("In the middle of the room there is a sole wooden table and a flickering candle on top of it.")
    print("East there is a massive steel door with a warning sign mounted on it and west there is a corridor leading into darkness.")
    while True:
        b = input()
        if b != "w" and b != "a" and b !="s" and b !="d":
            print("No valid input")
        elif b=="w" or b =="s":
            print("You can't move in this direction")
        elif b=="d":
            if key:
                print("You put the key into the key hole and slowly push the heavy door open.")
                print("You wake up in your bed and realize it was just a dream.")
                print()
                print("Thanks for playing!")
            else:
                print("The door is locked, you need a key to open it.")
        else:
            break
    if b=="a":
        print("You go back the corridor")
        room0()

def room2():
    print("You are an old prison lit by torches hanging on the wall.")
    print("To the north there is a prison cell, the iron bar door is left ajar. ")
    print("West you see a stair going even deeper down and east there is one going up.")
    while True:
        b = input()
        if b != "w" and b !="a" and b !="s" and b !="d":
            print("No valid input")
        elif b =="s":
            print("You can't move in this direction")
        else:
            break
    if b=="d":
        print("You go up the stone stair")
        room0()
    elif b=="a":
        print("You go down a stair into complete darkness when suddenly a shivering feeling comes over you. ")
        room4_dark()
    else:
        print("The door makes a loud screeching noise while you push it open.")
        room3()

def room3():
    print("The prison cell is empty, except for a corpse on the ground, you notice a dagger in the right its right hand")
    print("The exit is to the south")
    while True:
        b = input()
        if b != "w" and b !="a" and b !="s" and b !="d" and b != "dagger":
            print("No valid input")
        elif b =="a" or b =="w" or b =="d":
            print("You can't move in this direction")
        elif b == "dagger":
            print("You stole the dagger from the skeleton")
        else:
            break
    print("You leave the cell")
    room2()

def room4_dark():
    print("It is pitch black you can't even see your hands in front of your eyes.")
    while True:
        b = input()
        if b != "w" and b !="a" and b !="s" and b !="d" and b != "lamp":
            print("No valid input")
        elif b =="a" or b =="w" or b =="s":
            print("You can't move in this direction")
        else:
            break
    if b == "d":
        print("You carefully stumble back up the stairs")
        room2()

    else:
        print("You light up the lamp to see everything more clearly.")
        room4_fight()

def room4_fight():
    print("As you look up from the lamp you see an at least 3 meters tall beast with sharp claws showing its teeth.")
    print("Hello",player_name)
    print("The beast is preparing to punch with its huge hairy fists.")
    c = 0
    while True:
        c += 1
        b = input()
        if b != "w" and b != "a" and b != "s" and b != "d" and b != "lamp" and b != "dagger":
            print("You stand in shock and do nothing when the beast strikes you right in the face with its full force.")
            print("darkness")
            break
        elif b == "w" or b == "a" or b == "s":
            print("You try to dodge the attack but the beast is too fast and strikes you down with one punch.")
            print("The last few moments alive you witness yourself getting eaten alive.")
            break
        elif b == "d" and c == 1:
            print("You dodge the attack and run back up the stairway.")
            room2()
            break
        elif b == "dagger":
            if c == 1:
                print("You react quickly and pull the dagger out.")
                print("You duck under the furious punch and pierce the dagger right into the beasts knee, the beast jumps back with a loud battlecry.")
                print("You want to keep the beast at a distance before it charges again.")
            elif c == 2:
                print("The beast charges at you and you try to hit its knee again")
                print("But it expected the attack and throws you into a corner of the room.")
            else:
                print("You stand with your last energy and hold the dagger shakingly in the direction of the beast.")
                print("The beast roars with laughter before it picks you up and tears you apart.")
                break
        elif b == "lamp":
            if c == 1:
                print("In an attempt to keep the beast at distance you throw your lamp and you hit its face")
                print("You are in the dark again and start to think if it really was the best idea.")
                print("You never see the light again")
            else:
                print("You throw the lamp right on the beast's wounded knee.")
                print("The beast screams out a cry of pain and runs away into the darkness.")
                room4()

def room4():
    global key
    print("Since you destroyed the lamp you have no light anymore but you remember a chest that stood behind the beast.")
    while True:
        b = input()
        if b != "w" and b != "a" and b !="s" and b !="d" and b != "chest":
            print("No valid input")
        elif b == "w" or b == "a" or b == "s" or b == "d":
                print("You'll want to open the chest before you go.")
        else:
            print("You search the room and eventually you stumble over the chest.")
            print("You open the chest and inside you find an old rusty key.")
            key = True
            break
    room2()

#start
key = False
print("What is your name?")
player_name = input()
print("Hello",player_name,"and welcome to Dungeon, a TextBased Adventure Game")
input("Press Enter to continue")
print()

print("One night",player_name,"wakes up but not in his bed like normal but in a cold, creeping dungeon.")
print("It is really dark because the only thing illuminating the room is an old lamp sitting besides him. ")
print("Write the name of an item to pick it up or use it.")
a=input()
while a!= "lamp":
    print("No valid input")
    a=input()
print(player_name,"picks up the lamp")
a=input()
while a!= "lamp":
    print("No valid input")
    a=input()
print(player_name,"lights up the lamp.")
print()
print("Now you can see the room more clearly, you notice twines curling along the ceiling and skeletons with bashed skulls laying in chains against the wall.")
room0()