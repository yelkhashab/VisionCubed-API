from flask import Flask, jsonify, request
from flask_cors import CORS

# Assuming these modules are correctly set up
from src.face_scan import scan
from src.get_state import RubiksCube
from src.scrambler import generate_scramble
from src.solve import solve

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/api/scan', methods=['POST'])
def scan_image():
    image = request.get_json()  # Get the image data from the request
    # image = decode_image(image_data)  # Decode the image data
    result = scan(image)  # Call the scan function with the image
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

# @app.before_first_request
# def before_first_request():
#     print("The server is up and ready to handle requests!")

if __name__ == '__main__':
    app.run(debug=True)  