# Adjustable_Staircase
The design features predefined hole increments that enable controlled step adjustments, ensuring flexibility in experimental setups. The staircase accommodates multiple configurations while maintaining structural integrity, making it a valuable tool for biomechanical studies, gait analysis, and safety research.


![vlc-record-2025-03-17-18h45m56s-Recording 2025-03-17 184337 mp4-](https://github.com/user-attachments/assets/3cef2fa9-66fd-4dc2-b44e-c0abdb8e156b)



1️⃣Load Data:

  ⚫Reads an Excel file (Book1.xlsx) from the specified path.
  
  ⚫Extracts data from the sheet "ALL" for analysis.

2️⃣Prepare Variables for Regression:


  ⚫X: Slope (independent variable).
  
  ⚫y_tread: Tread dimension (dependent variable 1).
  
  ⚫y_riser: Riser dimension (dependent variable 2).


3️⃣Train Models:

  ⚫Trains two separate linear regression models for tread and riser using Slope as the predictor.

4️⃣User Input & Prediction:

  ⚫Asks the user to enter multiple slope values.
  
  ⚫Predicts the corresponding tread and riser values.
  
  ⚫Prints predictions in a readable format.
