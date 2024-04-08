import random

def generate_scramble(length=20):
    """
    Generates a Rubik's Cube scramble of specified length.
    
    Args:
    - length: The number of moves in the scramble. Default is 20.
    
    Returns:
    - A list of moves as a scramble.
    """
    moves = ['R', 'L', 'U', 'D', 'F', 'B']
    modifiers = ['', "'", '2']
    scramble = []
    last_move = ''
    
    while len(scramble) < length:
        move = random.choice(moves)
        if move == last_move:
            continue  # Avoid repeating the same move
        modifier = random.choice(modifiers)
        scramble.append(move + modifier)
        last_move = move
        
    return scramble

# Uncomment for testing
scramble = generate_scramble()
print(scramble)
