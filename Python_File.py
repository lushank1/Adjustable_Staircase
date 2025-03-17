import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the dataset (Ensure 'Book1.xlsx' is in the working directory)
file_path = "C:\\Users\\ACER\\AppData\\Roaming\\JetBrains\\PyCharmCE2024.3\\scratches\\Book1.xlsx"
df = pd.read_excel(file_path, sheet_name="ALL")

# Prepare the data
X = df[["Slope (approximately)"]]  # Independent variable (Slope)
y_tread = df["Tread (cm)"]  # Dependent variable 1 (Tread)
y_riser = df["Riser (cm)"]  # Dependent variable 2 (Riser)

# Train linear regression models
model_tread = LinearRegression().fit(X, y_tread)
model_riser = LinearRegression().fit(X, y_riser)

# Manual input for multiple slopes
try:
    slopes_input = input("Enter the slope angles in degrees (comma-separated): ")
    slope_values = np.array([[float(s)] for s in slopes_input.split(',')])

    # Predict values for multiple slopes
    predicted_treads = model_tread.predict(slope_values)
    predicted_risers = model_riser.predict(slope_values)

    # Print predictions
    for slope, tread, riser in zip(slope_values.flatten(), predicted_treads, predicted_risers):
        print(f"Predicted Tread (cm) at {slope:.2f}° slope: {tread:.2f} cm")
        print(f"Predicted Riser (cm) at {slope:.2f}° slope: {riser:.2f} cm\n")
except ValueError:
    print("Invalid input! Please enter numeric values separated by commas.")
