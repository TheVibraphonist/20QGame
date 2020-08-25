class Animals:
    def __init__(self, name, fur, tail, snout, gills, wings, claws, fourlegs, predator, scales, hoaves, teeth, beak, food):
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
    def __repr__(self):
        return self.name

NumGuess = 1
ListOfPAtributes = 'fur tail snout gills wings claws fourlegs, predator, scales, hoaves, teeth, beak, food'.split()
dog = Animals('dog', True, True, True, False, False, True, True, False, False, False, True, False, False)
clownfish = Animals('clown fish', False, True, False, True, False, False, False, False, True, False, False, False, False)
piranha = Animals('piranha', False, True, False, True, False, False, False, True, True, False, True, False, False)
human = Animals('human', True, False, False, False, False, True, False, False, False, False, True, False, False)
bluebird = Animals('bluebird', False, True, False, False, True, True, False, False, False, False, False, True, False)
falcon = Animals('falcon', False, True, False, False, True, True, False, True, False, False, False, True, False)
unicorn = Animals('unicorn', True, True, False, False, True, False, True, False, False, True, True, False, False)
duck = Animals('duck', False, True, False, False, True, True, False, False, False, False, True, True, True)
frog = Animals('frog', False, False, False, False, False, False, True, True, False, False, False, False, False)
bunny = Animals('bunny', True, True, False, False, False, False, True, False, False, False, True, False, False)
dragon = Animals('dragon', False, True, True, False, True, True, True, True, True, False, True, False, False)
Jayden = Animals('jayden', True, True, True, True, True, True, True, True, True, True, True, True, False)
worm = Animals('worm', False, True, False, False, False, False, False, False, False, False, False, False, False)



ListOfObjects = [dog, clownfish, human, bluebird, falcon, unicorn, piranha, duck, frog, bunny, dragon, Jayden, worm]
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
print(ListOfObjects)
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


