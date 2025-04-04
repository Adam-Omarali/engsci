"""
This is the image processing script. It allows you to take many measurments
of the length of various beads within an image using your mous to click on 
the head and tail of the flowing bead, and saves each data point from
image into a CSV with its X and Y coord, along with calculating the velocity
and uncertainty of the velocity using deltaV = V*sqrt((deltatime/time)**2 + 
(deltalength/length)**2), aka what we do in PHY293. Please makesure to keep all
your images in the images folder. to exit the Program and save the data to the
csv click ESC.

Input:  Image name ex: aer210.jpg
        Exposure Time ex: 163
        
Output: CSV file save in /csvs/


PLEASE make sure the length of the calibration bar is correct for your specific image,
for me this is 70.333 and 344, it might not be for you! If you wish to rewrite the csv, do it 
manually by deleting it or edditing it.
"""

import cv2
import numpy as np
import csv
import os

# Global variables to store clicked points
points = []

def click_event(event, x, y, flags, params):
    global points, pixel_to_um, frame_time, csv_file

    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 2:
            points.append((x, y))
            # Draw a circle at clicked point
            cv2.circle(image, (x, y), 3, (0, 255, 0), -1)
            cv2.imshow('Image', image)
            
            if len(points) == 2:
                # Draw line between points
                cv2.line(image, points[0], points[1], (0, 255, 0), 2)
                # Calculate length
                length_in_pixels = np.sqrt((points[1][0] - points[0][0])**2 + 
                                           (points[1][1] - points[0][1])**2)
                length_in_micrometers = length_in_pixels * pixel_to_um  # Convert to micrometers
                print(f"Length in pixels: {length_in_pixels:.2f}")
                print(f"Length in micrometers: {length_in_micrometers:.2f}")
                
                # Calculate velocity
                velocity = length_in_micrometers / frame_time  # μm/ms
                print(f"Velocity: {velocity:.2f} μm/ms")
                print(frame_time)
                # Calculate uncertainty
                dt = 0.1  # Uncertainty in time (ms)
                dd = (6)*pixel_to_um*2    # Uncertainty in distance (μm)
                delta_v = velocity*np.sqrt((dt/frame_time)**2 + 
                                  (dd/length_in_micrometers)**2)
                print(dt/frame_time)
                print(dd/length_in_micrometers)
                print(f"Velocity with uncertainty: {velocity:.2f} ± {delta_v:.2f} μm/ms")

                # Calculate average coordinates
                avg_x = (points[0][0] + points[1][0]) / 2
                avg_y = (points[0][1] + points[1][1]) / 2

                # Record measurement in CSV
                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([avg_x, avg_y, length_in_micrometers, velocity, delta_v])
                print(f"Recorded measurement: Avg X: {avg_x}, Avg Y: {avg_y}, Velocity: {velocity:.2f}, Uncertainty: {delta_v:.2f}")
                
                # Reset points for next measurement
                points.clear()
                print("Ready for next measurement. Click two new points.")

def line_length_analysis(image_path, scale_bar_length_um, scale_bar_pixel_length, csv_file_path):
    global image, points, pixel_to_um, frame_time, csv_file

    # Calculate scaling factor (μm per pixel)
    my_img_factor = 89.91 / 114.15
    # my_img_factor = 1
    pixel_to_um = scale_bar_length_um / scale_bar_pixel_length * my_img_factor  # micrometers per pixel
    csv_file = csv_file_path

    # Prepare CSV file
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Avg X", "Avg Y", "Length (μm)","Velocity (μm/ms)", "Uncertainty (μm/ms)"])  # Header row

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return

    while True:
        # Show the image and set mouse callback
        cv2.imshow('Image', image)
        cv2.setMouseCallback('Image', click_event)
        
        # Wait for a key press
        key = cv2.waitKey(0)
        if key == 27:  # ESC key to exit
            cv2.imwrite("annotated_img.png", image)
            print("Exiting program.")
            break

    cv2.destroyAllWindows()
    points = []  # Reset points for next use

# Example usage
image_path = "images/bend_64.5_smooth.jpg"  # Update with your image path
scale_bar_length_um = 200  # Length of the scale bar in micrometers YOU MIGHT HAVE TO CHANGE THIS
scale_bar_pixel_length = 461  # Scale bar length in pixels (measure it manually) YOU MIGHT HAVE TO CHANGE THIS
frame_time = float(input("Input the Exposure Time (ex: 69): "))  # Frame time in milliseconds
csv_file_path = f"csvs/{image_path[6:-4]}.csv"


line_length_analysis(image_path, scale_bar_length_um, scale_bar_pixel_length, csv_file_path)
