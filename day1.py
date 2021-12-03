
def solvePart1(inputPath):
    with open(inputPath) as f:
        lines = f.readlines()

    cleanLines = [int(a.replace('\n','')) for a in lines]

    diffs = [0] + [cleanLines[i] - cleanLines[i-1] for i in range(1,len(cleanLines))]

    bins = [1 if a > 0 else 0 for a in diffs]

    sums = sum(bins)

    return sums

def solvePart2(inputPath,rolling):
    with open(inputPath) as f:
        lines = f.readlines()

    cleanLines = [int(a.replace('\n','')) for a in lines]

    rollingSums = [sum(cleanLines[i-rolling:i]) for i in range(rolling,len(cleanLines)+1)]

    diffs = [rollingSums[i] - rollingSums[i-1] for i in range(1,len(rollingSums))]

    bins = [1 if a > 0 else 0 for a in diffs]

    sums = sum(bins)

    return sums

import pandas as pd
import numpy as np
def p2_pandas(inputPath,rolling):
    with open(inputPath) as f:
        lines = f.readlines()

    cleanLines = [int(a.replace('\n','')) for a in lines]

    df = pd.DataFrame({'ints':cleanLines}).rolling(rolling).sum().diff(1)

    # sums
    counts = len(df[df['ints'] > 0])

    print('solution using pandas: {}'.format(counts))

    return counts







puzzleInput = 'day0_input.txt'

p1Sol = solvePart1(puzzleInput)

print('part 1 solution: {}'.format(p1Sol))

p2Sol = solvePart2(puzzleInput,3)

print('part 2 solution: {}'.format(p2Sol))

p22 = p2_pandas(puzzleInput,3)

print('complete')