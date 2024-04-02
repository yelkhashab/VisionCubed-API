# VisionCubed
## Overview

This project aims to develop an interactive 3D Rubik's Cube solver that allows users to solve a Rubik's Cube puzzle with the aid of a computer vision model. By using a webcam, the application will recognize the current scrambled state of a Rubik's Cube, compute the optimal solution, and visually guide the user through each step of the solution with an animated 3D model.
Problem

### Problem

Many people are fascinated by Rubik's Cubes but find them challenging to solve. While numerous online solvers exist, they require manual input of the cube's state, which can be tedious and error-prone. This project addresses the need for an intuitive, automated solution that leverages technology to enhance the learning and solving experience.
User Profile

### User Profile

The primary users of this application are Rubik's Cube enthusiasts of all skill levels seeking an interactive and educational way to improve their solving techniques. The app is designed to be accessible to beginners while also offering value to experienced solvers interested in optimizing their strategies.
Features

### Features

Color Detection: Utilizes the cv2 library for computer vision to detect and categorize the colors of a scrambled Rubik's Cube.
Solution Algorithm: Integrates the Kociemba library to calculate the optimal solution steps.
3D Visualization: Renders a 3D model of the Rubik's Cube using Three.js or Spline, reflecting the initial scrambled state and animating the solution steps.
Interactive Controls: Allows users to play, pause, rewind, and fast-forward through the solution animation, facilitating a hands-on learning experience.

## Implementation
### Tech Stack

Frontend: React for building the user interface, Three.js/Spline for 3D modeling and animation.
Backend: Python Flask for handling the computer vision processing and solution computation.
Libraries: cv2 for color detection and image processing, Kociemba for solving algorithm, possibly Socket.IO for real-time communication between the frontend and backend.

### APIs

Webcam API: Access the user's webcam to capture images of the Rubik's Cube.
Custom API: Developed to communicate the cube's state and solution steps between the backend and the frontend.

### Sitemap

Home Page: Introduction and instructions on how to use the application.
Solver Page: Where users interact with the webcam feed, view the detected cube state, and follow along with the solution animation.
About Page: Information about the project, the technology used, and the developer.

### Mockups

(Mockups to be created using Figma, showing the layout of each page, including the webcam capture area, the 3D cube display, and controls for the solution animation.)
Data

### Data

The primary data involved are the color categories for each of the cube's faces, stored in an array format, and the sequence of moves required to solve the cube, represented as a string or series of steps.
Endpoints

### Endpoints

/detect-colors: POST, receives an image, returns an array of color categories.
/solve: POST, receives the array of faces, returns the solution steps.

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
Tutorial Mode: Guide users through solving the cube manually, step by step.

This proposal outlines a plan to create an innovative tool that combines computer vision, algorithms, and interactive 3D modeling to make solving Rubik's Cubes an engaging and educational experience.
