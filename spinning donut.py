import numpy as np
import os
import time

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function to render the spinning donut
def spinning_donut():
    # Constants for the torus
    A = 0  # Rotation angle around the X-axis
    B = 0  # Rotation angle around the Z-axis

    # Screen dimensions
    screen_width = 80
    screen_height = 40

    # Torus parameters
    R1 = 1  # Radius of the tube
    R2 = 2  # Distance from the center of the tube to the center of the torus

    # Precompute sine and cosine values for efficiency
    cosA = np.cos(A)
    sinA = np.sin(A)
    cosB = np.cos(B)
    sinB = np.sin(B)

    # Initialize the output grid
    def render_frame(A, B):
        # Create an empty screen buffer
        screen = [[' ' for _ in range(screen_width)] for _ in range(screen_height)]

        # Generate points on the torus
        theta = np.linspace(0, 2 * np.pi, 150)  # Angle around the tube
        phi = np.linspace(0, 2 * np.pi, 150)    # Angle around the torus

        # Precompute trigonometric values
        cosA = np.cos(A)
        sinA = np.sin(A)
        cosB = np.cos(B)
        sinB = np.sin(B)

        for th in theta:
            costh = np.cos(th)
            sinth = np.sin(th)

            for ph in phi:
                cosph = np.cos(ph)
                sinph = np.sin(ph)

                # Calculate the 3D coordinates of the point on the torus
                x = (R2 + R1 * costh) * cosph
                y = (R2 + R1 * costh) * sinph
                z = R1 * sinth

                # Apply rotations
                x_rotated = x * cosB - z * sinB
                y_rotated = y
                z_rotated = x * sinB + z * cosB

                x_final = x_rotated * cosA - y_rotated * sinA
                y_final = x_rotated * sinA + y_rotated * cosA
                z_final = z_rotated

                # Project to 2D
                ooz = 1 / (z_final + 5)  # Perspective projection
                xp = int(screen_width / 2 + 30 * ooz * x_final)
                yp = int(screen_height / 2 - 15 * ooz * y_final)

                # Check if the point is within screen bounds
                if 0 <= xp < screen_width and 0 <= yp < screen_height:
                    luminance = int(8 * ((cosph * costh * cosB - sinth * sinB) * cosA - cosph * costh * sinB - sinth * cosB - sinph * costh * sinA))
                    if luminance > 0:
                        screen[yp][xp] = ".,-~:;=!*#$@"[luminance]

        # Convert the screen buffer to a string and print it
        return '\n'.join(''.join(row) for row in screen)

    # Animation loop
    while True:
        clear_screen()
        print(render_frame(A, B))
        A += 0.07  # Increment rotation angles
        B += 0.03
        time.sleep(0.05)  # Control frame rate

if __name__ == "__main__":
    spinning_donut()