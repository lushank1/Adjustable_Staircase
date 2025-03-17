# Adjustable_Staircase
The design features predefined hole increments that enable controlled step adjustments, ensuring flexibility in experimental setups. The staircase accommodates multiple configurations while maintaining structural integrity, making it a valuable tool for biomechanical studies, gait analysis, and safety research.


![vlc-record-2025-03-17-18h45m56s-Recording 2025-03-17 184337 mp4-](https://github.com/user-attachments/assets/3cef2fa9-66fd-4dc2-b44e-c0abdb8e156b)



<p align="justify"> The design of the present staircase is based on the double-rocker mechanism is a four-bar linkage in which both the opposite links i.e., the coupler and a rocker undergo oscillatory motion rather than completing a full revolution.  Some of the research conducted are based on this process [10, 11] in which both the tread and riser dimension changes simultaneously.  The adjustable staircase with 10 steps is mounted in lab which have 8 holes of major four supporting rods as illustrated in Figure 1.  By shifting the placements of the single step by 2 and 4 holes upwards and downwards influences the dimensions of tread and riser.  The conventional size settings for the staircase is riser (R) and tread (T) at 45˚ slope as illustrated in Figure 2 (a).  The next combination is to expand the steps spacing by 10 holes and their corresponding tread and riser is measured as T2U and R2U, where 2U indicates the two holes above the original hole (U).  The next combination is to extend the spacing by 12 holes and distance between each hole is about equal to 100mm.  The next combination is to reduce the space between two steps, where the number of holes between two steps is 6.  The most effective combination is to lessen the gap by 4 holes.  Each combination demonstrates varied dimension of tread and riser at similar slope.  However, by adjusting the space between two steps the overall number of steps in staircase also fluctuate.  It is noteworthy to that as change in dimensions of slope the change in dimension of tread is significantly less than change in dimension of riser. </p>



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
