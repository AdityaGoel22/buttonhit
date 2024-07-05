# Button Hit

## Overview

This README file provides instruction and information about Button Hit game script that utilizies OpenCV and CVZone's Hand Tracking Module. The script creates a simple game where you can use your hand to interact with objects on the screen through your webcam

## Requirements

Before running this code, you need to have the following dependencies installed:
  1. Python
  2. OpenCV
  3. Cvzone
  4. NumPy

You can install these dependencies using pip:
```
pip install opencv-python cvzone numpy
```

## How to Run the Script

  1. **Connect Webcam**: Ensure your webcam is properly connected to your computer.
  2. **Run the Script**: Execute the script using the Python interpreter:
      ```
      python buttonHit.py
      ```
  3. **Gameplay**:
     * The game will start immediately upon running the script.
     * You will see a circle on the screen; your goal is to move your hand over the circle to "catch" it.
     * The distance from your hand to the circle is measured, and if your hand is close enough, your score increases.
     * The game lasts for a total of 20 seconds. Your final score will be displayed when the time is up.
     * Press the 'R' key to restart the game.

## Methodology
### Initialization
  * The webcam is initialized and the frame size is set to 1280x720.
  * A hand detector is created with a confidence threshold of 0.8 and set to detect a maximum of one hand.
  * A polynomial function is fitted to map distances to centimeters.

### Game Variables
  * cx, cy: Coordinates of the circle.
  * col: Color of the circle.
  * counter: Tracks the status of hand detection.
  * score: Player's score.
  * timestart: Time when the game starts.
  * totaltime: Total duration of the game (20 seconds).

### Main Loop
  * The script captures frames from the webcam, flips them, and processes them for hand detection.
  * If a hand is detected, the distance between specific points on the hand is calculated to determine the distance from the hand to the circle.
  * If the distance is less than 40 cm and the hand is over the circle, the score is incremented, and the circle's position is updated.
  * The remaining time and score are displayed on the screen.
  * If the time is up, a "Game Over" message and the final score are displayed.

### Restart Functionality
  * Pressing the 'R' key will reset the score and restart the game timer.

## Additional Information
* Ensure good lighting for better hand detection.
* Adjust the detection confidence and other parameters in the script if needed.


By following the instructions above, you can successfully run and play the Hand Tracking Game. Have fun!
