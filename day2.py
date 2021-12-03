from day1 import solvePart2


def loadPuzzleInput(puzzlePath):
    with open(puzzlePath) as f:
        lines = f.readlines()

    return lines

def solvePart1(puzzleList):
    # tuple of actions and values

    tups = [(s.split()[0],int(s.split()[1])) for s in puzzleList]

    horizontal = 0
    depth = 0

    for act,val in tups:
        if act == 'up':
            depth -= val
        elif act == 'down':
            depth += val
        else:
            horizontal += val

    # find product of both at end

    prod = horizontal * depth

    return prod

def solvePart2(puzzleList):
    tups = [(s.split()[0],int(s.split()[1])) for s in puzzleList]

    horizontal = 0
    depth = 0
    aim = 0

    # up and down now change aim and depth is changed by forward * aim

    for act, val in tups:
        if act == 'up':
            aim -= val

        elif act == 'down':
            aim += val

        else:
            horizontal += val
            depth += (val * aim)

    prod = depth * horizontal

    return prod

puzzlePath = 'day2_input.txt'

pLines = loadPuzzleInput(puzzlePath)

p1Sol = solvePart1(pLines)

print('part 1 solution: {}'.format(p1Sol))

p2Sol = solvePart2(pLines)

print('part 2 solution: {}'.format(p2Sol))

