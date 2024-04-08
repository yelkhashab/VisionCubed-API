def rotate_face_clockwise(face):
    """
    Rotates a face of the cube 90 degrees clockwise.
    """
    return [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]

def rotate_face_anticlockwise(face):
    """
    Rotates a face of the cube 90 degrees anticlockwise.
    """
    return [face[2], face[5], face[8], face[1], face[4], face[7], face[0], face[3], face[6]]

def update_state_for_move(self, move, modifier=""):
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
            new_state = update_state_for_r_move(self.state, rotation)
        elif move == 'L':
            new_state = update_state_for_l_move(self.state, rotation)
        elif move == 'U':
            new_state = update_state_for_u_move(self.state, rotation)
        elif move == 'D':
            new_state = update_state_for_d_move(self.state, rotation)
        elif move == 'F':
            new_state = update_state_for_f_move(self.state, rotation)
        elif move == 'B':
            new_state = update_state_for_b_move(self.state, rotation)
        
        return new_state

    # Apply the rotation
    new_state = rotate()
    
    if modifier == '2':
        self.state = new_state
        new_state = rotate()  # Apply the second rotation
    
    return new_state
    
def update_state_for_r_move(state, rotation):
    """
    Updates the cube state for an R move.
    """
    new_state = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        new_state['R'] = rotate_face_clockwise(state['R'])
        new_state['U'][2], new_state['U'][5], new_state['U'][8] = state['F'][2], state['F'][5], state['F'][8]
        new_state['F'][2], new_state['F'][5], new_state['F'][8] = state['D'][2], state['D'][5], state['D'][8]
        new_state['D'][2], new_state['D'][5], new_state['D'][8] = state['B'][6], state['B'][3], state['B'][0]
        new_state['B'][6], new_state['B'][3], new_state['B'][0] = state['U'][2], state['U'][5], state['U'][8]
    elif rotation == 'ACW':
        new_state['R'] = rotate_face_anticlockwise(state['R'])
        new_state['U'][2], new_state['U'][5], new_state['U'][8] = state['B'][6], state['B'][3], state['B'][0]
        new_state['B'][6], new_state['B'][3], new_state['B'][0] = state['D'][2], state['D'][5], state['D'][8]
        new_state['D'][2], new_state['D'][5], new_state['D'][8] = state['F'][2], state['F'][5], state['F'][8]
        new_state['F'][2], new_state['F'][5], new_state['F'][8] = state['U'][2], state['U'][5], state['U'][8]
    return new_state

def update_state_for_l_move(state, rotation):
    """
    Updates the cube state for an L move.
    """
    new_state = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        new_state['L'] = rotate_face_clockwise(state['L'])
        new_state['U'][0], new_state['U'][3], new_state['U'][6] = state['B'][8], state['B'][5], state['B'][2]
        new_state['F'][0], new_state['F'][3], new_state['F'][6] = state['U'][0], state['U'][3], state['U'][6]
        new_state['D'][0], new_state['D'][3], new_state['D'][6] = state['F'][0], state['F'][3], state['F'][6]
        new_state['B'][2], new_state['B'][5], new_state['B'][8] = state['D'][6], state['D'][3], state['D'][0]
    elif rotation == 'ACW':
        new_state['L'] = rotate_face_anticlockwise(state['L'])
        new_state['U'][0], new_state['U'][3], new_state['U'][6] = state['F'][0], state['F'][3], state['F'][6]
        new_state['F'][0], new_state['F'][3], new_state['F'][6] = state['D'][0], state['D'][3], state['D'][6]
        new_state['D'][0], new_state['D'][3], new_state['D'][6] = state['B'][8], state['B'][5], state['B'][2]
        new_state['B'][8], new_state['B'][5], new_state['B'][2] = state['U'][0], state['U'][3], state['U'][6]
    return new_state

def update_state_for_u_move(state, rotation):
    """
    Updates the cube state for a U move.
    """
    new_state = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        new_state['U'] = rotate_face_clockwise(state['U'])
        new_state['F'][0], new_state['F'][1], new_state['F'][2] = state['R'][0], state['R'][1], state['R'][2]
        new_state['R'][0], new_state['R'][1], new_state['R'][2] = state['B'][0], state['B'][1], state['B'][2]
        new_state['B'][0], new_state['B'][1], new_state['B'][2] = state['L'][0], state['L'][1], state['L'][2]
        new_state['L'][0], new_state['L'][1], new_state['L'][2] = state['F'][0], state['F'][1], state['F'][2]
    elif rotation == 'ACW':
        new_state['U'] = rotate_face_anticlockwise(state['U'])
        new_state['F'][0], new_state['F'][1], new_state['F'][2] = state['L'][0], state['L'][1], state['L'][2]
        new_state['R'][0], new_state['R'][1], new_state['R'][2] = state['F'][0], state['F'][1], state['F'][2]
        new_state['B'][0], new_state['B'][1], new_state['B'][2] = state['R'][0], state['R'][1], state['R'][2]
        new_state['L'][0], new_state['L'][1], new_state['L'][2] = state['B'][0], state['B'][1], state['B'][2] 
    return new_state

def update_state_for_d_move(state, rotation):
    """
    Updates the cube state for a D move.
    """
    new_state = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        new_state['D'] = rotate_face_clockwise(state['D'])
        new_state['F'][6], new_state['F'][7], new_state['F'][8] = state['L'][6], state['L'][7], state['L'][8]
        new_state['R'][6], new_state['R'][7], new_state['R'][8] = state['F'][6], state['F'][7], state['F'][8]
        new_state['B'][6], new_state['B'][7], new_state['B'][8] = state['R'][6], state['R'][7], state['R'][8]
        new_state['L'][6], new_state['L'][7], new_state['L'][8] = state['B'][6], state['B'][7], state['B'][8]
    elif rotation == 'ACW':
        new_state['D'] = rotate_face_anticlockwise(state['D'])
        new_state['F'][6], new_state['F'][7], new_state['F'][8] = state['R'][6], state['R'][7], state['R'][8]
        new_state['R'][6], new_state['R'][7], new_state['R'][8] = state['B'][6], state['B'][7], state['B'][8]
        new_state['B'][6], new_state['B'][7], state['B'][8] = state['L'][6], state['L'][7], state['L'][8]
        new_state['L'][6], new_state['L'][7], new_state['L'][8] = state['F'][6], state['F'][7], state['F'][8]
    return new_state

def update_state_for_f_move(state, rotation):
    """
    Updates the cube state for an F move.
    """
    new_state = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        new_state['F'] = rotate_face_clockwise(state['F'])
        new_state['U'][6], new_state['U'][7], new_state['U'][8] = state['L'][8], state['L'][5], state['L'][2]
        new_state['L'][2], new_state['L'][5], new_state['L'][8] = state['D'][0], state['D'][1], state['D'][2]
        new_state['D'][0], new_state['D'][1], new_state['D'][2] = state['R'][6], state['R'][3], state['R'][0]
        new_state['R'][0], new_state['R'][3], new_state['R'][6] = state['U'][6], state['U'][7], state['U'][8]
    elif rotation == 'ACW':
        new_state['F'] = rotate_face_anticlockwise(state['F'])
        new_state['U'][6], new_state['U'][7], new_state['U'][8] = state['R'][0], state['R'][3], state['R'][6]
        new_state['R'][0], new_state['R'][3], new_state['R'][6] = state['D'][0], state['D'][1], state['D'][2]
        new_state['D'][0], new_state['D'][1], new_state['D'][2] = state['L'][8], state['L'][5], state['L'][2]
        new_state['L'][2], new_state['L'][5], new_state['L'][8] = state['U'][6], state['U'][7], state['U'][8]
    return new_state

def update_state_for_b_move(state, rotation):
    """
    Updates the cube state for a B move.
    """
    new_state = {face: stickers[:] for face, stickers in state.items()}
    
    if rotation == 'CW':
        new_state['B'] = rotate_face_clockwise(state['B'])
        new_state['U'][0], new_state['U'][1], new_state['U'][2] = state['R'][2], state['R'][5], state['R'][8]
        new_state['L'][0], new_state['L'][3], new_state['L'][6] = state['U'][2], state['U'][1], state['U'][0]
        new_state['D'][6], new_state['D'][7], new_state['D'][8] = state['L'][0], state['L'][3], state['L'][6]
        new_state['R'][2], new_state['R'][5], new_state['R'][8] = state['D'][8], state['D'][7], state['D'][6]
    elif rotation == 'ACW':
        new_state['B'] = rotate_face_anticlockwise(state['B'])
        new_state['U'][0], new_state['U'][1], new_state['U'][2] = state['L'][6], state['L'][3], state['L'][0]
        new_state['R'][2], new_state['R'][5], new_state['R'][8] = state['U'][0], state['U'][1], state['U'][2]
        new_state['D'][6], new_state['D'][7], new_state['D'][8] = state['R'][2], state['R'][5], state['R'][8]
        new_state['L'][0], new_state['L'][3], new_state['L'][6] = state['D'][6], state['D'][7], state['D'][8]
    return new_state

class RubiksCube:
    def __init__(self, state=None):
        self.state = state or {
            'F': ['R']*9,
            'B': ['O']*9,
            'U': ['W']*9,
            'D': ['Y']*9,
            'L': ['G']*9,
            'R': ['B']*9,
        }
    
    def apply_move(self, move):
        move_type = move[0]  # Extract the move (e.g., 'R' from 'R' or 'R2')
        modifier = move[1:]  # Extract the modifier (e.g., "'" or '2')

        self.state = update_state_for_move(self, move_type, modifier)

    def apply_moves(self, moves):
        for move in moves:
            self.apply_move(move)

    def get_state(self):
        return self.state

# Testing the implementation
# cube = RubiksCube()
# cube.apply_moves(["F'", "R2", "U", "B", "L'", "D2"])
# state = cube.get_state()
# print(state)

