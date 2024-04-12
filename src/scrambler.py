import random

def generate_scramble(length=20):
    '''
    Generates a Rubik's Cube scramble of specified length.
    '''
    moves = ['R', 'L', 'U', 'D', 'F', 'B']
    modifiers = ['', "'", '2']
    scramble = []
    lastTwoMoves = ['X', 'Y']
    
    layerPairs = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U', 'F': 'B', 'B': 'F'}
    
    while len(scramble) < length:
        move = random.choice(moves)
        # Prevent using the same layer in immediate succession
        if move == lastTwoMoves[-1]:
            continue
        # Prevent making redundant moves
        if len(scramble) >= 1:
            if move == layerPairs[lastTwoMoves[-1]] and move == lastTwoMoves[-2]:
                continue
        modifier = random.choice(modifiers)
        fullMove = move + modifier
        scramble.append(fullMove)
        lastTwoMoves.pop(0)
        lastTwoMoves.append(move)
        print(lastTwoMoves)
    return scramble

# Uncomment for testing
scramble = generate_scramble()
print(scramble)
