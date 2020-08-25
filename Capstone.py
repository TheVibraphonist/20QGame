#    This is a 20Q game, in which you have to select an animal from the list of known animals, then the computer tries to guess which on you picked.
#    I have a total of 22 Questions right now. This is a functional 20Qs game written in python 3.
#    I used objects, list comprehension, list, and a total of 4 functions.

class Animals:
    def __init__(self, name, fur, tail, snout, gills, wings, claws, fourlegs, predator, scales, hoaves, teeth, beak, food, spine, legs, egg, vegetarian, carnivore, domestic, wild, fins, horns):
        self.name = name
        self.fur = fur
        self.tail = tail
        self.snout = snout
        self.gills = gills
        self.wings = wings
        self.claws = claws
        self.fourlegs = fourlegs
        self.predator = predator
        self.scales = scales
        self.hoaves = hoaves
        self.teeth = teeth
        self.beak = beak
        self.food = food
        self.spine = spine
        self.legs = legs
        self.egg = egg
        self.vege = vegetarian
        self.carn = carnivore
        self.domestic = domestic
        self.wild = wild
        self.fins = fins
        self.horns = horns
    def __repr__(self):
        return self.name

NumGuess = 1
ListOfPAtributes = 'fur tail snout gills wings claws fourlegs, predator, scales, hoaves, teeth, ' \
                   '\nbeak, food, spine, legs, egg, vegetarian, carnivore, domestic, wild, fins horns'.split()
dog = Animals('dog', True, True, True, False, False, True, True, False, False, False, True, False, False, True, True, False, False, True, True, False, False, False)
clownfish = Animals('clown fish', False, True, False, True, False, False, False, True, True, False, False, False, False, True, False, True, True, True, False, True, True, False)
piranha = Animals('piranha', False, True, False, True, False, False, False, True, True, False, True, False, False, True, False, True, False, True, False, True, True, False)
human = Animals('human', True, False, False, False, False, True, False, False, False, False, True, False, False, True, True, False, True, True, True, False, True, False)
bluebird = Animals('bluebird', False, True, False, False, True, True, False, False, False, False, False, True, False, True, True, True, True, True, False, True, False, False)
falcon = Animals('falcon', False, True, False, False, True, True, False, True, False, False, False, True, False, True, True, True, False, True, False, True, False, False)
unicorn = Animals('unicorn', True, True, False, False, True, False, True, False, False, True, True, False, False, True, True, False, True, True, False, True, False, True)
duck = Animals('duck', False, True, False, False, True, True, False, False, False, False, True, True, True, True, True, True, True, True, False, True, False, False)
frog = Animals('frog', False, False, False, False, False, False, True, True, False, False, False, False, False, True, True, True, False, True, False, True, False, False)
bunny = Animals('bunny', True, True, False, False, False, False, True, False, False, False, True, False, False, True, True, False, True, False, True, False, False, False)
camel = Animals('camel', True, True, True, False, False, False, True, False, False, True, True, False, False, True, True, False, True, False, True, False, False, False)
reindeer = Animals('reindeer', True, True, True, False, False, False, True, False, False, True, True, False, False, True, True, False, True, False, True, False, False, True)
armadillo = Animals('armadillo', False, True, True, False, False, True, True, True, False, False, True, False, False, True, True, True, False, True, False, True, False, False)



ListOfObjects = [dog, clownfish, human, bluebird, falcon, unicorn, duck, frog, piranha, bunny, camel, reindeer, armadillo]
def delet(dict, key):
    del dict[key]
    return dict

def getYesorNo(Qnumber):
    ans = input()
    ans = ans.lower().startswith('y')
    Qnumber +=1
    return ans, Qnumber

def WinorLose(win, lose):
    if not win and lose:
        print('good job you won!!')
        quit()
    elif win and not lose:
        print('aww, you lost. you suck.')
        quit()
    else:
        print('something went wrong. \n\n\n\n\n\n\n\n\n\n\n\n\n\n power off')
        quit()

def checkQuestionnum(Qnumber):
    if Qnumber <= 20:
        pass
    else:
        win = False
        lose = True
        WinorLose(win, lose)




print('please pick an animal.')
print(ListOfObjects, '\n\n\n')


print('does it have fur?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.fur == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.fur == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)


print('does it have a tail?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.tail == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.tail == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('does it have a snout?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.snout == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.snout == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('does it have gills?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.gills == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.gills == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('does it have wings?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.wings == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.wings == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('does it have claws?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.claws == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.claws == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('does it have fourlegs?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.fourlegs == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.fourlegs == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('is it a predator?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.predator == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.predator == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('does it have scales?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.scales == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.scales == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('does it have a hoof?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.hoaves == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.hoaves == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('does it have teeth?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.teeth == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.teeth == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)


print('does it have a beak?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.beak == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.beak == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)


print('is it food?  (not exotic foods)')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.scales == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.scales == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)



print('does it have a spine')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.spine == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.spine == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)




print('does it have legs?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.legs == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.legs == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)




print('does it lay an egg?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.egg == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.egg == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)




print('does it eat plants?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.vege == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.vege == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)




print('does it eat meat?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.carn == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.carn == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)




print('is it domesticated?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.domestic == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.domestic == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)




print('is it wild?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.wild == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.wild == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)




print('does it have fins?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.fins == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.fins == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)




print('does it have horns?')
TorF, NumGuess = getYesorNo(NumGuess)
if TorF:
    ListOfObjects = [i for i in ListOfObjects if i.horns == True]
elif not TorF:
    ListOfObjects = [i for i in ListOfObjects if i.horns == False]

if len(ListOfObjects) == 1:
    print('is it a ' + str(ListOfObjects) + '?')
    del ListOfObjects
    if input().lower().startswith('y'):
        win = True
        lose = False
        WinorLose(win, lose)
    elif input().lower().startswith('n'):
        print('well, i\'m completely stumped. \n\n Good Game!')

checkQuestionnum(NumGuess)




