from mcpi.minecraft import Minecraft
import pickle, os, time, random

mc = Minecraft.create()
if mc.getBlock(0, -1, 0) == 7:
    mc.postToChat("Well well well...")
    time.sleep(2)
    mc.postToChat("Looks like your in a 'pickle'")
    time.sleep(2)
    mc.postToChat("No need to worry, I got you :)")
    time.sleep(2)
    mc.postToChat("Rrrhhhhaahh!!")
    time.sleep(2)
    mc.postToChat("Done")
    mc.setBlock(0, -1, 0, 2)

if not os.path.exists('variables'):
    variables = {'blocksBroken': 0,
                 'level': 0}

    with open('variables', 'wb') as pickle_file:
        pickle.dump(variables, pickle_file)

with open('variables', 'rb') as pickle_file:
    variables = pickle.load(pickle_file)

blocksBroken = variables["blocksBroken"]

# define levels
def levelZero():
    mc.setBlock(0, -1, 0, 2)

def levelOne():
    block = [1, 2, 17, 18]

    mc.setBlock(0, -1, 0, block[random.randint(0, len(block)-1)])

def levelTwo():
    block = [1, 2, 3, 4, 5, 17]
    mc.setBlock(0, -1, 0, block[random.randint(0, len(block)-1)])

def levelThree():
    block = [1, 1, 1, 3, 4, 13, 15, 16]
    mc.setBlock(0, -1, 0, block[random.randint(0, len(block)-1)])

def levelFour():
    block = [1, 1, 1, 1, 1, 3, 4, 4, 13, 14, 15, 16, 16]
    mc.setBlock(0, -1, 0, block[random.randint(0, len(block)-1)])

def levelFive():
    block = [2, 3, 4, 6, 12, 12, 12, 12, 14, 14, 24, 24, 24, 24, 30, 81, 81]
    mc.setBlock(0, -1, 0, block[random.randint(0, len(block)-1)])

def levelSix():
    block = [3, 12, 12, 12, 13, 13, 13, 80, 82, 82, 83]
    mc.setBlock(0, -1, 0, block[random.randint(0, len(block)-1)])

def levelSeven():
    block = [1, 1, 1, 1, 1, 1, 1, 3, 4, 13, 13,
             14, 14, 15, 15, 16, 16, 16, 21, 56]
    mc.setBlock(0, -1, 0, block[random.randint(0, len(block)-1)])

def levelEight():
    block = [1, 2, 3, 4, 5, 6, 12, 13, 14, 15, 16,
             17, 18, 21, 24, 30, 35, 56, 81, 82, 83]
    mc.setBlock(0, -1, 0, block[random.randint(0, len(block)-1)])

while True:
    time.sleep(0)
    '#level up'
    if blocksBroken == 200 and variables["level"] != 8:
        mc.setBlock(0, -1, 0, 7)
        mc.postToChat("You are leveling up!")
        time.sleep(10)
        mc.setBlock(0, -1, 0, 0)
        blocksBroken = 0
        print(variables["level"])
        variables = {'blocksBroken': 0,
                     'level': variables["level"]+1}
        with open('variables', 'wb') as pickle_file:
            pickle.dump(variables, pickle_file)
        with open('variables', 'rb') as pickle_file:
            variables = pickle.load(pickle_file)

    '#set random block if 0, -1, 0 is air'
    if mc.getBlock(0, -1, 0) == 0:
        if variables["level"] == 0:
            levelZero()
        if variables["level"] == 1:
            levelOne()
        if variables["level"] == 2:
            levelTwo()
        if variables["level"] == 3:
            levelThree()
        if variables["level"] == 4:
            levelFour()
        if variables["level"] == 5:
            levelFive()
        if variables["level"] == 6:
            levelSix()
        if variables["level"] == 7:
            levelSeven()
        if variables["level"] == 8:
            levelEight()
        blocksBroken += 1