# VisionCubed
## Running the Project Locally

Follow these steps to run the project on your local machine:

1. **Clone the repository to your local machine**

    ```bash
    git clone https://github.com/yelkhashab/VisionCubed-API.git
    ```

2. **Navigate to the project directory**

    ```bash
    cd VisionCubed-API
    ```

3. **Create a virtual environment**

    On macOS and Linux:

    ```bash
    python3 -m venv venv
    ```

    On Windows:

    ```bash
    py -m venv venv
    ```

4. **Activate the virtual environment**

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

    On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

5. **Install the requirements**

    ```bash
    pip install -r requirements.txt
    ```

6. **Copy the sample Flask environment file and adjust if necessary**

    ```bash
    cp .flaskenv_sample .flaskenv
    ```

7. **Run the Flask application**

    ```bash
    flask run
    ```

After running this command, you should see output indicating that the server is running. You can access the application at `http://localhost:8080` in your web browser.

## Overview

This project aims to develop an interactive 3D Rubik's Cube solver that allows users to solve a Rubik's Cube puzzle with the aid of a computer vision model. By using a webcam, the application will recognize the current scrambled state of a Rubik's Cube, compute the optimal solution, and visually guide the user through each step of the solution with an animated 3D model.

### Problem

Many people are fascinated by Rubik's Cubes but find them challenging to solve. While numerous online solvers exist, they require manual input of the cube's state, which can be tedious and error-prone. This project addresses the need for an intuitive, automated solution that leverages technology to enhance the learning and solving experience.

### User Profile

The primary users of this application are Rubik's Cube enthusiasts of all skill levels seeking an interactive and educational way to improve their solving techniques. The app is designed to be accessible to beginners while also offering value to experienced solvers interested in optimizing their strategies.

### Features

Color Detection: Utilizes the cv2 library for computer vision to detect and categorize the colors of a scrambled Rubik's Cube.  
Solution Algorithm: Integrates the Kociemba library to calculate the optimal solution steps.  
Scramble Algorithm: Generates a random set of moves to scramble a cube.  
3D Visualization: Renders a 3D model of the Rubik's Cube using Three.js or Spline, reflecting the initial scrambled state and animating the solution steps.    

## Implementation
### Tech Stack

Frontend: React for building the user interface, Three.js for 3D modeling and animation.  
Backend: Python Flask for handling the computer vision processing and solution computation. 
Libraries: cv2 for color detection and image processing, Kociemba for solving algorithm, roofpig.js for 3D cube render and animation

### APIs

Custom API: Developed to communicate the cube's state and solution steps between the backend and the frontend.  

### Sitemap

Home Page:  
			Start page with navigation links and a prompt to get started. 
     
Solve Page:  
			Where users interact with the webcam feed, view the detected cube state, and follow along with the solution animation.  
     
Practice Page:  
			The user can generate a scramble then start a timer to practice solving the cube and track progression.  

### Mockups

### Home Page

![VisionCubed Mockup-1](https://github.com/yelkhashab/VisionCubed/assets/88597501/8cca8ac7-ad86-419d-8912-7cf4b764f3ce)

### Solve

![VisionCubed Solve 1](https://github.com/yelkhashab/VisionCubed/assets/88597501/a60cfa60-eff4-4b89-a6a0-9991dfbced29)
![VisionCubed Solve 2](https://github.com/yelkhashab/VisionCubed/assets/88597501/bafd15b3-6c5f-4cf5-859c-0e83150a86b3)

### Practice

![VisionCubed Practice 1](https://github.com/yelkhashab/VisionCubed/assets/88597501/3a821e5f-ebe6-4ff4-8691-0d3783068347)
![VisionCubed Practice 2](https://github.com/yelkhashab/VisionCubed/assets/88597501/6020f578-5ab8-44aa-bce6-6de641887b87)

### Data

The primary data involved are the colors for each of the cubies on the cube's faces, stored in an array format, and the sequence of moves required to solve the cube, represented as a string or series of steps.

### Endpoints

/scan: POST, receives an image, returns an array of faces and colors.  
/solve: POST, receives the array of faces, returns the solution steps.  
/scramble: GET, returns a set of moves to scramble a cube.  

### Auth

No authentication is required for this version of the application.

## Roadmap

Week 1:  
    - Initial setup of the computer vision model.  
    - Integration of the Kociemba library and development of the backend solution logic.  
    
Week 2:  
    - Development of the frontend, including 3D modeling and animation.  
    - Integration between frontend and backend, testing. 
      
Week 3:  
    - Final touches, deployment, and documentation.  

## Nice-to-haves

User Account System: Allow users to save and track their progress over time.  
Leaderboard: For users to compare solving times or the number of moves.  
Cube Variety: Allow users to use the tool to solve multiple types of cubes (2x2, 4x4, ...).  
Interactive Controls: Allows users to play, pause, rewind, and fast-forward through the solution animation, facilitating a hands-on learning experience.  
Select Solving Algorithm: Allows the user to select from a list of solving methods/algorithms. Ranges from slow but easy to optimal but difficult.
