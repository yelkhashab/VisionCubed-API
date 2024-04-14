def rotateFaceClockwise(face):
    """
    Rotates a face of the cube 90 degrees clockwise.
    """
    return [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]

def rotateFaceAnticlockwise(face):
    """
    Rotates a face of the cube 90 degrees anticlockwise.
    """
    return [face[2], face[5], face[8], face[1], face[4], face[7], face[0], face[3], face[6]]

def updateStateForMove(self, move, modifier=""):
    """
    Update the cube state for a given move, applying clockwise or anticlockwise rotations as needed.
    
    Args:
    - move: The move to be applied (e.g., 'R', 'L').
    - modifier: The modifier for the move ('', "'", '2').
    """

    if modifier == "'":
        rotation = 'ACW'
    else:
        rotation = 'CW'

    def rotate():
        if move == 'R':
            newState = updateStateForRMove(self.state, rotation)
        elif move == 'L':
            newState = updateStateForLMove(self.state, rotation)
        elif move == 'U':
            newState = updateStateForUMove(self.state, rotation)
        elif move == 'D':
            newState = updateStateForDMove(self.state, rotation)
        elif move == 'F':
            newState = updateStateForFMove(self.state, rotation)
        elif move == 'B':
            newState = updateStateForBMove(self.state, rotation)
        
        return newState

    # Apply the rotation
    newState = rotate()
    self.state = newState
    
    if modifier == '2':
        newState = rotate()  # Apply the second rotation
        self.state = newState
    
    return newState
    
def updateStateForRMove(state, rotation):
    """
    Updates the cube state for an R move.
    """
    newState = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        newState['R'] = rotateFaceClockwise(state['R'])
        newState['U'][2], newState['U'][5], newState['U'][8] = state['F'][2], state['F'][5], state['F'][8]
        newState['F'][2], newState['F'][5], newState['F'][8] = state['D'][2], state['D'][5], state['D'][8]
        newState['D'][2], newState['D'][5], newState['D'][8] = state['B'][6], state['B'][3], state['B'][0]
        newState['B'][6], newState['B'][3], newState['B'][0] = state['U'][2], state['U'][5], state['U'][8]
    elif rotation == 'ACW':
        newState['R'] = rotateFaceAnticlockwise(state['R'])
        newState['U'][2], newState['U'][5], newState['U'][8] = state['B'][6], state['B'][3], state['B'][0]
        newState['B'][6], newState['B'][3], newState['B'][0] = state['D'][2], state['D'][5], state['D'][8]
        newState['D'][2], newState['D'][5], newState['D'][8] = state['F'][2], state['F'][5], state['F'][8]
        newState['F'][2], newState['F'][5], newState['F'][8] = state['U'][2], state['U'][5], state['U'][8]
    return newState

def updateStateForLMove(state, rotation):
    """
    Updates the cube state for an L move.
    """
    newState = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        newState['L'] = rotateFaceClockwise(state['L'])
        newState['U'][0], newState['U'][3], newState['U'][6] = state['B'][8], state['B'][5], state['B'][2]
        newState['F'][0], newState['F'][3], newState['F'][6] = state['U'][0], state['U'][3], state['U'][6]
        newState['D'][0], newState['D'][3], newState['D'][6] = state['F'][0], state['F'][3], state['F'][6]
        newState['B'][2], newState['B'][5], newState['B'][8] = state['D'][6], state['D'][3], state['D'][0]
    elif rotation == 'ACW':
        newState['L'] = rotateFaceAnticlockwise(state['L'])
        newState['U'][0], newState['U'][3], newState['U'][6] = state['F'][0], state['F'][3], state['F'][6]
        newState['F'][0], newState['F'][3], newState['F'][6] = state['D'][0], state['D'][3], state['D'][6]
        newState['D'][0], newState['D'][3], newState['D'][6] = state['B'][8], state['B'][5], state['B'][2]
        newState['B'][8], newState['B'][5], newState['B'][2] = state['U'][0], state['U'][3], state['U'][6]
    return newState

def updateStateForUMove(state, rotation):
    """
    Updates the cube state for a U move.
    """
    newState = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        newState['U'] = rotateFaceClockwise(state['U'])
        newState['F'][0], newState['F'][1], newState['F'][2] = state['R'][0], state['R'][1], state['R'][2]
        newState['R'][0], newState['R'][1], newState['R'][2] = state['B'][0], state['B'][1], state['B'][2]
        newState['B'][0], newState['B'][1], newState['B'][2] = state['L'][0], state['L'][1], state['L'][2]
        newState['L'][0], newState['L'][1], newState['L'][2] = state['F'][0], state['F'][1], state['F'][2]
    elif rotation == 'ACW':
        newState['U'] = rotateFaceAnticlockwise(state['U'])
        newState['F'][0], newState['F'][1], newState['F'][2] = state['L'][0], state['L'][1], state['L'][2]
        newState['R'][0], newState['R'][1], newState['R'][2] = state['F'][0], state['F'][1], state['F'][2]
        newState['B'][0], newState['B'][1], newState['B'][2] = state['R'][0], state['R'][1], state['R'][2]
        newState['L'][0], newState['L'][1], newState['L'][2] = state['B'][0], state['B'][1], state['B'][2] 
    return newState

def updateStateForDMove(state, rotation):
    """
    Updates the cube state for a D move.
    """
    newState = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        newState['D'] = rotateFaceClockwise(state['D'])
        newState['F'][6], newState['F'][7], newState['F'][8] = state['L'][6], state['L'][7], state['L'][8]
        newState['R'][6], newState['R'][7], newState['R'][8] = state['F'][6], state['F'][7], state['F'][8]
        newState['B'][6], newState['B'][7], newState['B'][8] = state['R'][6], state['R'][7], state['R'][8]
        newState['L'][6], newState['L'][7], newState['L'][8] = state['B'][6], state['B'][7], state['B'][8]
    elif rotation == 'ACW':
        newState['D'] = rotateFaceAnticlockwise(state['D'])
        newState['F'][6], newState['F'][7], newState['F'][8] = state['R'][6], state['R'][7], state['R'][8]
        newState['R'][6], newState['R'][7], newState['R'][8] = state['B'][6], state['B'][7], state['B'][8]
        newState['B'][6], newState['B'][7], newState['B'][8] = state['L'][6], state['L'][7], state['L'][8]
        newState['L'][6], newState['L'][7], newState['L'][8] = state['F'][6], state['F'][7], state['F'][8]
    return newState

def updateStateForFMove(state, rotation):
    """
    Updates the cube state for an F move.
    """
    newState = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        newState['F'] = rotateFaceClockwise(state['F'])
        newState['U'][6], newState['U'][7], newState['U'][8] = state['L'][8], state['L'][5], state['L'][2]
        newState['L'][2], newState['L'][5], newState['L'][8] = state['D'][0], state['D'][1], state['D'][2]
        newState['D'][0], newState['D'][1], newState['D'][2] = state['R'][6], state['R'][3], state['R'][0]
        newState['R'][0], newState['R'][3], newState['R'][6] = state['U'][6], state['U'][7], state['U'][8]
    elif rotation == 'ACW':
        newState['F'] = rotateFaceAnticlockwise(state['F'])
        newState['U'][6], newState['U'][7], newState['U'][8] = state['R'][0], state['R'][3], state['R'][6]
        newState['R'][0], newState['R'][3], newState['R'][6] = state['D'][0], state['D'][1], state['D'][2]
        newState['D'][0], newState['D'][1], newState['D'][2] = state['L'][2], state['L'][5], state['L'][8]
        newState['L'][2], newState['L'][5], newState['L'][8] = state['U'][6], state['U'][7], state['U'][8]
    return newState

def updateStateForBMove(state, rotation):
    """
    Updates the cube state for a B move.
    """
    newState = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        newState['B'] = rotateFaceClockwise(state['B'])
        newState['U'][0], newState['U'][1], newState['U'][2] = state['R'][2], state['R'][5], state['R'][8]
        newState['L'][0], newState['L'][3], newState['L'][6] = state['U'][2], state['U'][1], state['U'][0]
        newState['D'][6], newState['D'][7], newState['D'][8] = state['L'][0], state['L'][3], state['L'][6]
        newState['R'][2], newState['R'][5], newState['R'][8] = state['D'][8], state['D'][7], state['D'][6]
    elif rotation == 'ACW':
        newState['B'] = rotateFaceAnticlockwise(state['B'])
        newState['U'][0], newState['U'][1], newState['U'][2] = state['L'][6], state['L'][3], state['L'][0]
        newState['R'][2], newState['R'][5], newState['R'][8] = state['U'][0], state['U'][1], state['U'][2]
        newState['D'][6], newState['D'][7], newState['D'][8] = state['R'][8], state['R'][5], state['R'][2]
        newState['L'][0], newState['L'][3], newState['L'][6] = state['D'][6], state['D'][7], state['D'][8]
    return newState

class RubiksCube:
    def __init__(self, state=None):
        self.state = state or {
            'F': ['G']*9,
            'B': ['B']*9,
            'U': ['W']*9,
            'D': ['Y']*9,
            'L': ['O']*9,
            'R': ['R']*9,
        }
    
    def applyMove(self, move):
        moveType = move[0]  # Extract the move (e.g., 'R' from 'R' or 'R2')
        modifier = move[1:]  # Extract the modifier (e.g., "'" or '2')

        self.state = updateStateForMove(self, moveType, modifier)

    def applyMoves(self, moves):
        for move in moves:
            self.applyMove(move)

    def getState(self):
        return self.state

# Testing the implementation
# cube = RubiksCube()
# cube.applyMoves(["U'", 'B2', "F'", 'R', 'B', 'D2', 'R2', 'U', "D'", 'U', 'R', 'B', 'F2', "B'", "U'", 'B', 'R', 'U2', 'R', "B'"])
# state = cube.getState()
# print(state)
