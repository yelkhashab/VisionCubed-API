import kociemba

def convertToNet(state):
    order = ['U', 'R', 'F', 'D', 'L', 'B']
    net = ''
    conversion_dict = {'W': 'U', 'B': 'R', 'R': 'F', 'Y': 'D', 'G': 'L', 'O': 'B'}
    for face in order:
        net += ''.join([conversion_dict[letter] for letter in state[face]])
    return net

# state =  {'F': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9'], 'B': ['O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9'], 'U': ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9'], 'D': ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9'], 'L': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'], 'R': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']}
# state = {'F': ['R' for i in range(9)], 'B': ['O' for i in range(9)], 'U': ['W' for i in range(9)], 'D': ['Y' for i in range(9)], 'L': ['G' for i in range(9)], 'R': ['B' for i in range(9)]}
# state = {'F': ['W', 'B', 'Y', 'W', 'R', 'Y', 'B', 'R', 'G'], 'B': ['W', 'Y', 'G', 'R', 'O', 'W', 'O', 'R', 'G'], 'U': ['R', 'B', 'B', 'G', 'W', 'R', 'R', 'O', 'B'], 'D': ['Y', 'B', 'O', 'O', 'Y', 'W', 'R', 'Y', 'W'], 'L': ['Y', 'Y', 'B', 'B', 'G', 'O', 'W', 'G', 'R'], 'R': ['O', 'W', 'O', 'O', 'B', 'G', 'Y', 'G', 'G']}
# print("State: ", state)
# print("Kociemba State: ", convertToNet(state))
# print("Kociemba Solution: ", solve(state))