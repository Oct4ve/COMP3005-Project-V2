# COMP3005 Project V2
Sam Wilson 101195493

Hello, This is my submission for COMP3005 Final Project. This was done on my own in a group of 1.

This is a Health & Fitness App where members can log in or register using email and password. Members can then do the following things:
    - Update their Personal Info
    - View the Dashboard
        - View/Update their Health Metrics (Height, Weight, etc.)
        - View Goals
        - View Routines
    - Book/Cancel sessions with a Trainer
    - Enroll in or leave classes

Trainers can also be added or deleted by staff members. Trainers can do the following things:
    - Create/Delete booking times (Trainers create timeslots for themselves and members can book those timeslots)
    - See member info (View all Members or Search through Members)

Staff can do the following things:
    - Add/Delete/Update Equipment
    - Create/Cancel Classes
    - Add/Delete Trainers
    - View/Create/Delete/Update Bills

Included are the following files:
	- DDL File to create the database
	- DML File to populate the database for testing purposes
		* Note that Members, Goals, Bookings, Bills, Routines should not be inserted using SQL. These things should only be created by
		use of the program itself. Inserting with SQL can lead to problems.
	- Python source code (HEALTHFITNESSAPP.py)
	- Image of ER Diagram
	- README.TXT

To run this program:
  - First ensure that psycopg2 is installed: type the following into command prompt

		pip install psycopg2

  - Open HEALTHFITNESSAPP.py and ensure that in connect_to_db() the credentials are correct.
  - Run the application by navigating to the directory containing the source code and typing into the command prompt:

        	python HEALTHFITNESSAPP.py
