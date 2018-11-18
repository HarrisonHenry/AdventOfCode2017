with open('day1input') as puzzleInputFile:
    puzzleInput = list(puzzleInputFile.read())

puzzleInput = tuple((int(x) for x in puzzleInput))

solution = 0

for i, num in enumerate(puzzleInput):
    if puzzleInput[i] == puzzleInput[(i+1) % len(puzzleInput)]:
        solution += num

print(solution)
