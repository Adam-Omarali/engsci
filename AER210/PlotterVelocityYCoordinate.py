
"""
This program reads a given CSV file in the /csvs/ folder and plots
velocity on the X and Y coordinate on the Y. This is most useful
for thr striaght section. 

Input: csv file name ex: aer210.csv
Output: Plot inlc uncertainties no trendline.
"""

import matplotlib.pyplot as plt
import csv
import os
import scipy.optimize
import numpy as np

pixel_to_micrometer = 200/461
dy = 10 * pixel_to_micrometer
dl = 6 * 2 * pixel_to_micrometer
dt = 0.1
exposure = 48.2


def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

def plot_velocity_vs_y(csv_file):
    # Check if the file exists
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' not found.")
        return

    # Initialize lists to store data
    velocities = []
    lengths = []
    y_coordinates = []

    # Read data from CSV
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                velocities.append(float(row["Velocity (μm/ms)"]))
                lengths.append(float(row["Length (μm)"]))
                y_coordinates.append(float(row["Avg Y"]) * pixel_to_micrometer)
            except KeyError:
                print("Error: CSV file does not contain the required columns.")
                return
            except ValueError:
                print("Error: Could not convert data to float.")
                return
            
    
    velocity_errors = np.array(velocities)*np.sqrt((dt/exposure)**2 + 
                    (dl/np.array(lengths))**2)
            
    coeff, covar = scipy.optimize.curve_fit(quadratic, y_coordinates, velocities)
    y_fit = np.linspace(min(y_coordinates), max(y_coordinates), 500)
    v_fit = quadratic(y_fit, *coeff)
    #get uncertainty in best fit parameters
    perr = np.sqrt(np.diag(covar))
    
    # Residuals
    residuals = velocities - quadratic(np.array(y_coordinates), *coeff)

    # R^2 calculation
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((velocities - np.mean(velocities))**2)
    r_squared = 1 - (ss_res / ss_tot)

    # Reduced chi^2 calculation
    # If you have uncertainties, replace 1 with your sigma values
    sigma = velocity_errors
    chi_squared = np.sum((residuals / sigma)**2)
    degrees_of_freedom = len(velocities) - len(coeff)
    reduced_chi_squared = chi_squared / degrees_of_freedom

    print(f"R^2: {r_squared}")
    print(f"Reduced Chi^2: {reduced_chi_squared}")

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.plot(y_fit, v_fit, color='red', label='Quadratic fit')
    plt.errorbar(
        y_coordinates,
        velocities,
        xerr=dy,
        yerr=velocity_errors,
        fmt='o',
        color='blue',
        ecolor='red',
        elinewidth=1,
        capsize=3,
        label='Data points with error bars'
    )
    plt.ylabel('Velocity (μm/ms)', fontsize=14)
    plt.xlabel('Y Coordinate (μm)', fontsize=14)
    plt.title('Y Coordinate vs. Velocity', fontsize=16)
    equation_text = f'Fit: $v = {coeff[0]:.2f}y^2 + {coeff[1]:.2f}y + {coeff[2]}$'
    plt.text(10, 7, equation_text, fontsize=12, color='blue')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # Ask user for the CSV file path
    csv_file = "csvs/profile_plot_straight_48.2_20cm.csv"  # e.g., genericname.csv
    plot_velocity_vs_y(csv_file)

if __name__ == "__main__":
    main()
