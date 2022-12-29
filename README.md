# Tracking_Objects
A simple Pygame progam including tracking objects.

=== DESCRIPTION ===
This program is a simple program that uses concepts such as acceleration, velocity, and displacement to create several tracking objects that home in on the user's mouse. For each tracker, it moves towards the mouse, accelerating and adjusting course if it overshoots (which it constantly does because of the way acceleration and velocity work). If it hits an edge, it loops around to the other side of the screen. Right clicking at any time resets the velocities of all objects and freezes them until the right mouse button is no longer held.

The program itself has no goal, and is merely a showcase of how to build tracking objects for other games in Pygame.

=== INSTRUCTIONS ===
To run the program:
1. Run main.py

To edit the background colour or change the number of trackers or the properties of the trackers:
For background colour, find the backgroundColour variable in the class "Game" located in the main.py file and change it there.

To change the properties or number of trackers, go to "self.ballStats" in the class "Game" (it should be a 2D array). Each array item held in the "ballStats" array is a tracker. The parameters are listed from left to right as so:
- Starting X
- Starting Y
- Colour
- Size
- Maximum Acceleration (higher means the tracker will be albe to turn more sharply and it will reach top speed much quicker)
- Maximum Velocity (higher means the tracker will have a much higher top speed, but may struggle to turn as effectively)

Removing an array removes the associated tracker, while adding a new array adds another tracker.

=== USAGE ===
Feel free to use the tracker's code in any of your own programs. Simply open "actors.py" and copy the "Ball" class, which holds all of the code for actual tracker movement (for just the code handling the movement, look for the "updatePosition" function).
