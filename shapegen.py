import cv2
import numpy as np

# Video dimensions
width = 640
height = 480

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('moving_rectangle.avi', fourcc, 20.0, (width, height))

# Initial position of the rectangle
x = 0
y = 0

# Speed and direction of the rectangle
speed_x = 5
speed_y = 2

# Size of the rectangle
rect_width = 50
rect_height = 30

while True:
    # Create a white background
    frame = np.full((height, width, 3), 255, dtype=np.uint8)
    
    # Draw a black rectangle
    cv2.rectangle(frame, (x, y), (x + rect_width, y + rect_height), (0, 0, 0), -1)
    
    # Write the frame
    out.write(frame)
    
    # Display the frame
    cv2.imshow('Video', frame)
    
    # Move the rectangle
    x += speed_x
    y += speed_y
    
    # Change direction if the rectangle reaches the boundaries
    if x <= 0 or x + rect_width >= width:
        speed_x = -speed_x
    if y <= 0 or y + rect_height >= height:
        speed_y = -speed_y
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when done
out.release()
cv2.destroyAllWindows()
