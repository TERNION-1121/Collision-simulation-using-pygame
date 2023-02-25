# Collision Simulation using pygame
A program simulation to learn pygame :p

<img src="https://user-images.githubusercontent.com/97667653/221360793-201c31b4-69e8-42c3-b584-91d4e8a2d259.png" height = 400 width = 400>

### `class Circle():`

It creates a circle object, for simplicity of the program we are having 2 circles on a **800 * 800** window.

Class methods for `Circle()`:
1. `drawCircle()`: It draws the circle with the given coordinates on the pygame window.
2. `moveCircle()`: It increases the x and y coordinates of the circle with the given velocities.

`checkCollision()`
It checks for collision between the two circles

> Here collision means: if the distance between the radii of the two circles is less than or equal to the sum of their radii
