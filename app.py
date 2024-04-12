from flask import Flask, jsonify, request
from flask_cors import CORS

# Assuming these modules are correctly set up
from src.cubeScanner import scan
from src.getState import RubiksCube
from src.scrambler import generateScramble
from src.solve import solve

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/api/scan', methods=['POST'])
def scan_image():
    images = request.get_json()
    
    # Extract the base64-encoded images from the request
    raw_images = [images['F'], images['R'], images['B'], images['L'], images['U'], images['D']]

    result = scan(raw_images)  # Call the scan function with the raw_images
    if 'unknown' in result:
        return jsonify({'error': 'Error scanning'}), 400  # Return 400 error code if result contains 'unknown'
    return jsonify(result)  # Return the result as a JSON response

@app.route('/api/scramble', methods=['GET'])
def api_scramble():
    scramble = generate_scramble()
    cube = RubiksCube()  # Create a new cube
    cube.apply_moves(scramble)  # Apply the scramble to the cube
    state = cube.get_state()
    print("Scramble: ", scramble)
    print("State: ", state)
    return jsonify({'scramble': scramble, 'state': state})  # Make sure to return serializable data

@app.route('/api/solve', methods=['POST'])
def api_solve():
    state = request.get_json()  # Get the state dictionary from the request
    solution = solve(state)  # Call the solve function with the state dictionary
    return jsonify({'solution': solution})  # Return the result as a JSON response

if __name__ == '__main__':
    app.run(debug=True)  