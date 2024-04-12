import kociemba

def convertToNet(state):
    '''
    This function takes a dictionary of faces where each face is represented
    by an array of nine cubies and their colors. The cubies are ordered as shown
    in the net below. It replaces the colors with the letters U, R, F, D, L, and B, 
    which stand for Up, Right, Front, Down, Left, and Back, respectively to allow 
    for solving from any starting orientation.

                     |------------|
                     | U1  U2  U3 |
                     |            |
                     | U4  U5  U6 |
                     |            |
                     | U7  U8  U9 |
        |------------|------------|------------|------------|
        | L1  L2  L3 | F1  F2  F3 | R1  R2  R3 | B1  B2  B3 |
        |            |            |            |            |
        | L4  L5  L6 | F4  F5  F6 | R4  R5  R6 | B4  B5  B6 |
        |            |            |            |            |
        | L7  L8  L9 | F7  F8  F9 | R7  R8  R9 | B7  B8  B9 |
        |------------|------------|------------|------------|
                     | D1  D2  D3 |
                     |            |
                     | D4  D5  D6 |
                     |            |
                     | D7  D8  D9 |
                     |------------|

    The function returns a string that represents the state of the cube in the 
    format that Kociemba's algorithm expects. The pieces are ordered as follows:
    U1U2U3...R1R2R3...F1F2F3...D1D2D3...L1L2L3...B1B2B3...
    '''
    order = ['U', 'R', 'F', 'D', 'L', 'B']
    net = ''
    colorToFace = {
        'W': 'U',
        'B': 'R',
        'R': 'F',
        'Y': 'D',
        'G': 'L',
        'O': 'B'
    }
    
    for face in order:
        net += ''.join([colorToFace[letter] for letter in state[face]])
    return net

def solve(state):
    net = convertToNet(state)
    return kociemba.solve(net)

# state =  {'F': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9'], 'B': ['O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9'], 'U': ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9'], 'D': ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9'], 'L': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], 'R': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']}
# state = {'F': ['R' for i in range(9)], 'B': ['O' for i in range(9)], 'U': ['W' for i in range(9)], 'D': ['Y' for i in range(9)], 'L': ['G' for i in range(9)], 'R': ['B' for i in range(9)]}
# state = {'F': ['W', 'B', 'Y', 'W', 'R', 'Y', 'B', 'R', 'G'], 'B': ['W', 'Y', 'G', 'R', 'O', 'W', 'O', 'R', 'G'], 'U': ['R', 'B', 'B', 'G', 'W', 'R', 'R', 'O', 'B'], 'D': ['Y', 'B', 'O', 'O', 'Y', 'W', 'R', 'Y', 'W'], 'L': ['Y', 'Y', 'B', 'B', 'G', 'O', 'W', 'G', 'R'], 'R': ['O', 'W', 'O', 'O', 'B', 'G', 'Y', 'G', 'G']}
# print("State: ", state)
# print("Kociemba State: ", convertToNet(state))
# print("Kociemba Solution: ", solve(state))