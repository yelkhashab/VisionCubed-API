import cv2
import numpy as np
import base64
import math

def decode_image(base64_image):
    """
    This function takes a base64-encoded string and decodes it as an image,
    converts it to the appropriate colour space (CIELAB) for colour
    recognition, and returns a cropped version of it so that individual pieces
    can later be extracted.
    """
    
    encoded_image = np.frombuffer(base64.b64decode(base64_image), dtype=np.uint8)
    decoded_image = cv2.imdecode(encoded_image, 1)
    converted_image = cv2.cvtColor(decoded_image, cv2.COLOR_BGR2LAB)

    # crop to 144x144 (so we can have 3 48x48 rows/columns)
    cropped_image = converted_image[17:161, 45:189]

    return cropped_image

def standardize_colour_scheme(face, colour_scheme, center_piece):
    """
    This function takes the given colour scheme dictionary and maps the colour
    of the given center piece with the colour that it is supposed to represent.
    """
    # take the midpoint of the piece and determine its L, a, and b values
    # according to the CIELAB standard
    center_midpoint = center_piece[24, 24]
    center_midpoint = (center_midpoint[0] / 2.55,
                       center_midpoint[1] - 128,
                       center_midpoint[2] - 128)

    face_order = ["R", "B", "O", "G", "W", "Y"]
    colour_scheme[face_order[face]] = center_midpoint

def identify_colour(square, colour_scheme):
    """
    This function takes pixel values in CIELAB format from a specific square
    and compares it to the preestablished colour scheme, determining which of
    the six colours it is closest to.

    source: http://colormine.org/delta-e-calculator
    """
    closest_colour = ""
    best_delta = math.inf

    square_midpoint = square[24, 24]
    square_midpoint = (square_midpoint[0] / 2.55,
                       square_midpoint[1] - 128,
                       square_midpoint[2] - 128)

    # apply colour difference algorithm against all 6 known colours and keep
    # the closest
    for colour in colour_scheme:
        known_lab = colour_scheme[colour]
        delta = math.sqrt(((known_lab[0] - square_midpoint[0]) ** 2) +
                          ((known_lab[1] - square_midpoint[1]) ** 2) +
                          ((known_lab[2] - square_midpoint[2]) ** 2))

        if delta < best_delta:
            best_delta = delta
            closest_colour = colour

    return closest_colour

def scan(raw_images):
    colours = [[[None, None, None], [None, None, None], [None, None, None]],
               [[None, None, None], [None, None, None], [None, None, None]],
               [[None, None, None], [None, None, None], [None, None, None]],
               [[None, None, None], [None, None, None], [None, None, None]],
               [[None, None, None], [None, None, None], [None, None, None]],
               [[None, None, None], [None, None, None], [None, None, None]]]

    colour_scheme = {}

    # first, we can standardize a colour scheme
    for face in range(6):
        image = decode_image(raw_images[face])

        # do this by looking at the center piece of each face
        center_piece = image[48:96, 48:96]
        standardize_colour_scheme(face, colour_scheme, center_piece)

    # then, we can use it to determine each piece's colour
    for face in range(6):
        image = decode_image(raw_images[face])

        for row in range(3):
            for column in range(3):

                # cut each face into 48x48 squares and identify their colour
                square = image[(row * 48):((row + 1) * 48), (column * 48):((column + 1) * 48)]
                colours[face][row][column] = identify_colour(square, colour_scheme)

    cube_state = {
        'F': colours[0][0] + colours[0][1] + colours[0][2],
        'R': colours[1][0] + colours[1][1] + colours[1][2],
        'B': colours[2][0] + colours[2][1] + colours[2][2],
        'L': colours[3][0] + colours[3][1] + colours[3][2],
        'U': colours[4][0] + colours[4][1] + colours[4][2],
        'D': colours[5][0] + colours[5][1] + colours[5][2],
    }

    return cube_state

