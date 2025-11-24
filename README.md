# Water-Intake-Tracker
A simple Python project to track daily water intake using glasses, ml and litre modes.

# Overview

A simple Python project that helps users track their daily water intake.  
The program supports *three input modes* — Glasses, Millilitres (ml), and Litres.  
It calculates the total water consumed, compares it with the daily target,  
and gives a hydration status. The project also stores history in a text file.

# Features

- Choose intake mode:
  - *Glass mode* (1 glass = 0.25 L)
  - *ml mode* (convert ml → litres automatically)
  - *Litre mode*
- Takes water intake for:
  - Morning
  - Afternoon
  - Evening
- Calculates total intake in litres
- Compares with target and shows hydration level:
  - Very Low  
  - Low  
  - Almost Reached  
  - Target Achieved  
  - Over Drinking
- Saves all records in a file: water_history.txt
- Option to view full history

# Technologies Used

- *Python 3*
- File Handling  
- Conditional Statements  and logic
- Functions  

# How to Run the Project
1.Install Python 3(If not installed).

2.Download all project files:

 -water_tracker.py
 
-water_history.txt(automatically created) 

 3. Run the program

 #Testing Instructions
Try running the project with different modes:

#Glass Mode Example

- Target: 8 glasses  
- Morning: 2  
- Afternoon: 3  
- Evening: 2  

#ml Mode Example

- Target: 2000 ml  
- Morning: 500 ml  
- Afternoon: 700 ml  
- Evening: 600 ml  

#Litre Mode Example

- Target: 2.5 litres  
- Morning: 1.0  
- Afternoon: 0.8  
- Evening: 0.4  

Check the file water_history.txt to ensure records are saved.

# Made by:
Chinmay Jain  
B.Tech CSE Core  
VIT Bhopal University

# Note
This project is created for the VIT Bhopal Python Course Project Submission
as per the official guidelines.
