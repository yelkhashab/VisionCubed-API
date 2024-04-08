def rotate_face_clockwise(face):
    """
    Rotates a face of the cube 90 degrees clockwise.
    """
    return [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]

def update_state_for_r_move(state):
    """
    Updates the cube state for an R move.
    """
    new_state = {face: stickers[:] for face, stickers in state.items()}  # Deep copy of the state
    new_state['R'] = rotate_face_clockwise(state['R'])
    new_state['U'][2], new_state['U'][5], new_state['U'][8] = state['F'][2], state['F'][5], state['F'][8]
    new_state['F'][2], new_state['F'][5], new_state['F'][8] = state['D'][2], state['D'][5], state['D'][8]
    new_state['D'][2], new_state['D'][5], new_state['D'][8] = state['B'][6], state['B'][3], state['B'][0]
    new_state['B'][0], new_state['B'][3], new_state['B'][6] = state['U'][2], state['U'][5], state['U'][8]
    return new_state

def update_state_for_u_move(state):
    """
    Updates the cube state for a U move.
    """
    new_state = {face: stickers[:] for face, stickers in state.items()}  # Deep copy of the state
    new_state['U'] = rotate_face_clockwise(state['U'])
    new_state['F'][:3], new_state['R'][:3], new_state['B'][:3], new_state['L'][:3] = state['R'][:3], state['B'][:3], state['L'][:3], state['F'][:3]
    return new_state

def update_state_for_f_move(state):
    """
    Updates the cube state for an F move.
    """
    new_state = {face: stickers[:] for face, stickers in state.items()}  # Deep copy of the state
    new_state['F'] = rotate_face_clockwise(state['F'])
    new_state['U'][6], new_state['U'][7], new_state['U'][8] = state['L'][8], state['L'][5], state['L'][2]
    new_state['L'][2], new_state['L'][5], new_state['L'][8] = state['D'][0], state['D'][1], state['D'][2]
    new_state['D'][0], new_state['D'][1], new_state['D'][2] = state['R'][6], state['R'][3], state['R'][0]
    new_state['R'][0], new_state['R'][3], new_state['R'][6] = state['U'][6], state['U'][7], state['U'][8]
    return new_state

# Updating the RubiksCube class to include corrected move implementations
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
        if move == 'R':
            self.state = update_state_for_r_move(self.state)
        elif move == 'U':
            self.state = update_state_for_u_move(self.state)
        elif move == 'F':
            self.state = update_state_for_f_move(self.state)
        # Add other moves as needed
    
    def apply_moves(self, moves):
        for move in moves:
            self.apply_move(move)

    def get_state(self):
        return self.state


