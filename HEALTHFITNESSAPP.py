import psycopg2
from psycopg2 import sql
from datetime import date, datetime


# Function to establish a connection to the PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="Sam's Health & Fitness App",
            user="postgres",
            password="daethaENdgrFAt",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)


# Displays all members
def get_all_members():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error retrieving members:", e)
    finally:
        cursor.close()
        conn.close()


# Adds a new member to the system
def add_member(first_name, last_name, email, phone, date_of_birth, join_date, password):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        insert_query = sql.SQL(
            "INSERT INTO members (first_name, last_name, email, phone, date_of_birth, join_date, password) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(insert_query, (first_name, last_name, email, phone, date_of_birth, join_date, password))
        conn.commit()
        print("Student added successfully.")
    except psycopg2.Error as e:
        print("Error adding student:", e)
    finally:
        cursor.close()
        conn.close()


# adds 7 empty days for the specified member
def add_days_for_member(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for day in days_of_week:
            insert_query = sql.SQL("INSERT INTO days (day, member_id) VALUES (%s, %s)")
            cursor.execute(insert_query, (day, member_id))

        conn.commit()
        print("Days added successfully.")

    except psycopg2.Error as e:
        print("Error adding days:", e)

    finally:
        cursor.close()
        conn.close()


def display_days(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT days.day, routines.routine_name
            FROM days
            LEFT JOIN routines ON days.routine_id = routines.routine_id
            WHERE days.member_id = %s
            ORDER BY 
                CASE
                    WHEN days.day = 'Monday' THEN 1
                    WHEN days.day = 'Tuesday' THEN 2
                    WHEN days.day = 'Wednesday' THEN 3
                    WHEN days.day = 'Thursday' THEN 4
                    WHEN days.day = 'Friday' THEN 5
                    WHEN days.day = 'Saturday' THEN 6
                    WHEN days.day = 'Sunday' THEN 7
                    ELSE 8
                END
        """)

        cursor.execute(query, (member_id,))
        days = cursor.fetchall()

        if days:
            print(f"Days for Member ID {member_id}:")
            for day in days:
                print(f"Day: {day[0]}")
                print(f"Routine Name: {day[1]}")
                print("------")
        else:
            print("No days found for member.")

    except psycopg2.Error as e:
        print("Error displaying days:", e)
    finally:
        cursor.close()
        conn.close()


# Updates email of the specified member
def update_member_attribute(member_id, attribute_name, new_value):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        update_query = sql.SQL("""
            UPDATE members
            SET {} = %s
            WHERE member_id = %s
        """).format(sql.Identifier(attribute_name))

        cursor.execute(update_query, (new_value, member_id))

        conn.commit()
        print(f"{attribute_name} updated successfully.")

    except psycopg2.Error as e:
        print(f"Error updating {attribute_name}:", e)
    finally:
        cursor.close()
        conn.close()


# Updates the date of birth of the specified member
def update_member_date_of_birth(member_id, new_date_of_birth):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        update_query = sql.SQL("""
            UPDATE members
            SET date_of_birth = %s
            WHERE member_id = %s
        """)

        cursor.execute(update_query, (new_date_of_birth, member_id))

        conn.commit()
        print("Date of birth updated successfully.")

    except psycopg2.Error as e:
        print("Error updating date of birth:", e)
    finally:
        cursor.close()
        conn.close()


# Updates the join date of the specified member
def update_member_join_date(member_id, new_join_date):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        update_query = sql.SQL("""
            UPDATE members
            SET join_date = %s
            WHERE member_id = %s
        """)

        cursor.execute(update_query, (new_join_date, member_id))

        conn.commit()
        print("Join date updated successfully.")

    except psycopg2.Error as e:
        print("Error updating join date:", e)
    finally:
        cursor.close()
        conn.close()


# Deletes the specified member
def delete_member(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        delete_query = sql.SQL("DELETE FROM members WHERE member_id = %s")
        cursor.execute(delete_query, (member_id,))
        conn.commit()
        print("Member deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting member:", e)
    finally:
        cursor.close()
        conn.close()


# Displays the attributes of the specified member
def display_member(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT * FROM members WHERE member_id = %s
        """)

        cursor.execute(query, (member_id,))
        member = cursor.fetchone()

        if member:
            print("Member ID:", member[0])
            print("First Name:", member[1])
            print("Last Name:", member[2])
            print("Email:", member[3])
            print("Phone:", member[4])
            print("Date of Birth:", member[5])
            print("Join Date:", member[6])
            # Password is not displayed for security reasons
        else:
            print("Member not found.")

    except psycopg2.Error as e:
        print("Error displaying member:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all trainers
def get_all_trainers():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trainers")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error retrieving trainers:", e)
    finally:
        cursor.close()
        conn.close()


# Adds a trainer to the list of trainers
def add_trainer(first_name, last_name, email, phone, password):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        insert_query = sql.SQL(
            "INSERT INTO trainers (first_name, last_name, email, phone, password) VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(insert_query, (first_name, last_name, email, phone, password))
        conn.commit()
        print("Trainer added successfully.")
    except psycopg2.Error as e:
        print("Error adding trainer:", e)
    finally:
        cursor.close()
        conn.close()


# Delete specified trainer
def delete_trainer(trainer_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        delete_query = sql.SQL("DELETE FROM trainers WHERE trainer_id = %s")
        cursor.execute(delete_query, (trainer_id,))
        conn.commit()
        print("Trainer deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting trainer:", e)
    finally:
        cursor.close()
        conn.close()


# add an EMPTY health metrics member for a certain id
def add_health_metrics(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        insert_query = sql.SQL("INSERT INTO health_metrics (member_id) VALUES (%s)")
        cursor.execute(insert_query, (member_id,))
        conn.commit()
        print("Health metrics added successfully.")
    except psycopg2.Error as e:
        print("Error adding health metrics:", e)
    finally:
        cursor.close()
        conn.close()


# delete health metrics for a member
def delete_health_metrics(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        delete_query = sql.SQL("DELETE FROM health_metrics WHERE member_id = %s")
        cursor.execute(delete_query, (member_id,))
        conn.commit()
        print("Health metrics deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting health metrics:", e)
    finally:
        cursor.close()
        conn.close()


# updates a health metric.
def update_health_metric(member_id, metric_name, new_value):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        update_query = sql.SQL("UPDATE health_metrics SET {} = %s WHERE member_id = %s").format(
            sql.Identifier(metric_name))
        cursor.execute(update_query, (new_value, member_id))
        conn.commit()
        print("Health metric {} updated successfully.".format(metric_name))
    except psycopg2.Error as e:
        print("Error updating health metric:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all health metrics for the specified member
def display_health_metrics(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT * FROM health_metrics WHERE member_id = %s
        """)

        cursor.execute(query, (member_id,))
        health_metrics = cursor.fetchone()

        if health_metrics:
            print("Member ID:", health_metrics[0])
            print("Height (cm):", health_metrics[1] if health_metrics[1] is not None else "Not recorded")
            print("Weight (kg):", health_metrics[2] if health_metrics[2] is not None else "Not recorded")
            print("Resting Heart Rate (bpm):", health_metrics[3] if health_metrics[3] is not None else "Not recorded")
            print("Body Fat Percentage:", health_metrics[4] if health_metrics[4] is not None else "Not recorded")
        else:
            print("Health metrics not found for member.")

    except psycopg2.Error as e:
        print("Error displaying health metrics:", e)
    finally:
        cursor.close()
        conn.close()


# adds a goal row for the specified member
def add_goal(member_id, goal_name):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            INSERT INTO goals (member_id, goal) VALUES (%s, %s)
        """)

        cursor.execute(query, (member_id, goal_name))
        conn.commit()
        print("Goal added successfully.")

    except psycopg2.Error as e:
        print("Error adding goal:", e)
    finally:
        cursor.close()
        conn.close()


# deletes a goal row for the specified member
def delete_goal(goal_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            DELETE FROM goals WHERE goal_id = %s
        """)

        cursor.execute(query, (goal_id,))
        conn.commit()
        print("Goal deleted successfully.")

    except psycopg2.Error as e:
        print("Error deleting goal:", e)
    finally:
        cursor.close()
        conn.close()


# Updates all goals under the specified member. UNUSED. Doesn't work as intended.
def update_goal(member_id, new_goal):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        update_query = sql.SQL("UPDATE goals SET goal = %s WHERE member_id = %s")
        cursor.execute(update_query, (new_goal, member_id))
        conn.commit()
        print("Goal updated successfully.")
    except psycopg2.Error as e:
        print("Error updating goal:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all goals for the specified member
def display_goals(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT * FROM goals WHERE member_id = %s
        """)

        cursor.execute(query, (member_id,))
        goals = cursor.fetchall()

        if goals:
            print(f"Goals for Member ID {member_id}:")
            for goal in goals:
                print(f"Goal ID: {goal[0]}")
                print(f"Goal: {goal[2]}")
                print("------")
        else:
            print("No goals found for member.")

    except psycopg2.Error as e:
        print("Error displaying goals:", e)
    finally:
        cursor.close()
        conn.close()


# Enrolls the specified member into the specified class.
def enroll_in_class(member_id, class_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        insert_query = sql.SQL("INSERT INTO class_enrollments (class_id, member_id) VALUES (%s, %s)")
        cursor.execute(insert_query, (class_id, member_id))

        conn.commit()
        print("Member enrolled in class successfully.")

    except psycopg2.Error as e:
        print("Error enrolling member in class:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all classes that the specified member is enrolled in
def view_enrolled_classes(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        select_query = sql.SQL("""
            SELECT c.class_id, c.trainer_id, c.class_date, c.start_time, c.end_time
            FROM classes c
            JOIN class_enrollments ce ON c.class_id = ce.class_id
            WHERE ce.member_id = %s
        """)

        cursor.execute(select_query, (member_id,))

        enrolled_classes = cursor.fetchall()

        print(f"All Enrolled Classes for Member ID {member_id}:")
        for cls in enrolled_classes:
            print("Class ID:", cls[0])
            print("Trainer ID:", cls[1])
            print("Class Date:", cls[2])
            print("Start Time:", cls[3])
            print("End Time:", cls[4])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error retrieving enrolled classes:", e)
    finally:
        cursor.close()
        conn.close()


# Unenrolls the specified member from the specified class
def leave_class(member_id, class_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        delete_query = sql.SQL("""
            DELETE FROM class_enrollments
            WHERE member_id = %s AND class_id = %s
        """)

        cursor.execute(delete_query, (member_id, class_id))

        conn.commit()
        print("Member left the class successfully.")

    except psycopg2.Error as e:
        print("Error leaving class:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all available classes
def display_all_classes():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT * FROM classes
        """)

        cursor.execute(query)
        classes = cursor.fetchall()

        if classes:
            print("All Classes:")
            for cls in classes:
                print(f"Class ID: {cls[0]}")
                print(f"Trainer ID: {cls[1]}")
                print(f"Class Date: {cls[2]}")
                print(f"Start Time: {cls[3]}")
                print(f"End Time: {cls[4]}")
                print("------")
        else:
            print("No classes found.")

    except psycopg2.Error as e:
        print("Error displaying classes:", e)
    finally:
        cursor.close()
        conn.close()


# Books the specified booking for the specified member.
def book_with_trainer(member_id, booking_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Check if booking exists
        check_query = sql.SQL("""
            SELECT booking_id FROM bookings
            WHERE booking_id = %s
        """)

        cursor.execute(check_query, (booking_id,))
        existing_booking = cursor.fetchone()

        if not existing_booking:
            print("No booking with that ID.")
            return

        # Update booking with new member
        update_query = sql.SQL("""
            UPDATE bookings
            SET member_id = %s
            WHERE booking_id = %s
        """)

        cursor.execute(update_query, (member_id, booking_id))

        conn.commit()
        print("Booking successful.")

    except psycopg2.Error as e:
        print("Error updating booking:", e)
    finally:
        cursor.close()
        conn.close()


# Cancels the specified booking, making the booking available again
def cancel_trainer(booking_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        update_query = sql.SQL("""
            UPDATE bookings
            SET member_id = NULL
            WHERE booking_id = %s
        """)

        cursor.execute(update_query, (booking_id,))

        conn.commit()
        print("Booking canceled successfully.")

    except psycopg2.Error as e:
        print("Error canceling booking:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all bookings that are not yet taken
def view_available_bookings():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        select_query = sql.SQL("""
            SELECT * FROM bookings
            WHERE member_id IS NULL
        """)

        cursor.execute(select_query)

        available_bookings = cursor.fetchall()

        print("Available Bookings:")
        for booking in available_bookings:
            print("Booking ID:", booking[0])
            print("Trainer ID:", booking[1])
            print("Booking Date:", booking[2])
            print("Start Time:", booking[3])
            print("End Time:", booking[4])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error retrieving available bookings:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all available bookings that are run by the specified trainer
def view_trainer_availability(trainer_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        select_query = sql.SQL("""
            SELECT * FROM bookings
            WHERE trainer_id = %s AND member_id IS NULL
        """)

        cursor.execute(select_query, (trainer_id,))

        trainer_bookings = cursor.fetchall()

        print(f"Available Bookings for Trainer ID {trainer_id}:")
        for booking in trainer_bookings:
            print("Booking ID:", booking[0])
            print("Booking Date:", booking[2])
            print("Start Time:", booking[3])
            print("End Time:", booking[4])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error retrieving trainer availability:", e)
    finally:
        cursor.close()
        conn.close()


# Schedules the specified routine name for the specified day for the specified member.
def schedule_routine(member_id, day, routine_name):
    # Check if the provided day is valid
    valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day not in valid_days:
        print("Invalid input. Please provide a valid day (Monday, Tuesday, ... Sunday).")
        return
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Insert a new routine into the routines table
        insert_routine_query = sql.SQL("""
            INSERT INTO routines (routine_name, member_id)
            VALUES (%s, %s)
            RETURNING routine_id
        """)

        cursor.execute(insert_routine_query, (routine_name, member_id))
        routine_id = cursor.fetchone()[0]  # Get the newly created routine_id

        # Update the day with the new routine_id
        update_query = sql.SQL("""
            UPDATE days
            SET routine_id = %s
            WHERE member_id = %s AND day = %s
        """)

        cursor.execute(update_query, (routine_id, member_id, day))

        conn.commit()
        print("Routine scheduled successfully.")

    except psycopg2.Error as e:
        print("Error scheduling routine:", e)
    finally:
        cursor.close()
        conn.close()


# Removes the routine from the specified day for the specified member
def cancel_routine(member_id, day):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        update_query = sql.SQL("""
            UPDATE days
            SET routine_id = NULL
            WHERE member_id = %s AND day = %s
        """)

        cursor.execute(update_query, (member_id, day))

        conn.commit()
        print("Routine canceled successfully.")

    except psycopg2.Error as e:
        print("Error canceling routine:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all classes run by the specified trainer.
def get_trainer_classes(trainer_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        select_query = sql.SQL("""
            SELECT * FROM classes
            WHERE trainer_id = %s
        """)

        cursor.execute(select_query, (trainer_id,))

        classes = cursor.fetchall()

        print(f"All Classes for Trainer ID {trainer_id}:")
        for cls in classes:
            print("Class ID:", cls[0])
            print("Trainer ID:", cls[1])
            print("Class Date:", cls[2])
            print("Start Time:", cls[3])
            print("End Time:", cls[4])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error retrieving classes by trainer_id:", e)
    finally:
        cursor.close()
        conn.close()


# Gets all bookings (taken or available) for the specified trainer.
def get_bookings(trainer_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        select_query = sql.SQL("SELECT * FROM bookings WHERE trainer_id = %s")
        cursor.execute(select_query, (trainer_id,))

        bookings = cursor.fetchall()

        print(f"All Bookings for Trainer ID {trainer_id}:")
        for booking in bookings:
            print("Booking ID:", booking[0])
            print("Trainer ID:", booking[1])
            print("Booking Date:", booking[2])
            print("Booking Start Time:", booking[3])
            print("Booking End Time:", booking[4])
            print("Member ID:", booking[5])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error retrieving bookings:", e)
    finally:
        cursor.close()
        conn.close()


# Creates a booking for the specified time for the specified trainer (available by default)
def add_booking(trainer_id, booking_date, start_time, end_time):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Check for time conflicts
        query = sql.SQL("""
            SELECT booking_id FROM bookings
            WHERE trainer_id = %s
            AND (
                (booking_start < %s AND booking_end > %s)
                OR (booking_start < %s AND booking_end > %s)
                OR (booking_start >= %s AND booking_end <= %s)
            )
        """)

        cursor.execute(query, (trainer_id, start_time, start_time, end_time, end_time, start_time, end_time))
        conflicting_bookings = cursor.fetchall()

        if conflicting_bookings:
            print("Time conflict detected with existing bookings. Please choose a different time.")
            return

        # If no time conflict, insert the new booking
        insert_query = sql.SQL("""
            INSERT INTO bookings (trainer_id, booking_date, booking_start, booking_end)
            VALUES (%s, %s, %s, %s)
        """)

        cursor.execute(insert_query, (trainer_id, booking_date, start_time, end_time))
        conn.commit()
        print("Booking added successfully.")

    except psycopg2.Error as e:
        print("Error adding booking:", e)
    finally:
        cursor.close()
        conn.close()


# Cancels the specified booking, whether taken or available
def remove_booking(booking_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        delete_query = sql.SQL("DELETE FROM bookings WHERE booking_id = %s")
        cursor.execute(delete_query, (booking_id,))

        conn.commit()
        print("Booking removed successfully.")

    except psycopg2.Error as e:
        print("Error removing booking:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all equipment
def get_all_equipment():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        select_query = sql.SQL("SELECT * FROM equipment")
        cursor.execute(select_query)

        equipment_list = cursor.fetchall()

        print("Equipment:")
        for equipment in equipment_list:
            print("Equipment ID:", equipment[0])
            print("Equipment Name:", equipment[1])
            print("Last Maintained:", equipment[2])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error retrieving equipment:", e)
    finally:
        cursor.close()
        conn.close()


# Adds equipment with the specified name
def add_equipment(equipment_name, last_maintained):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        insert_query = sql.SQL("INSERT INTO equipment (equipment_name, last_maintained) VALUES (%s, %s)")
        cursor.execute(insert_query, (equipment_name, last_maintained))
        conn.commit()
        print("Equipment added successfully.")
    except psycopg2.Error as e:
        print("Error adding equipment:", e)
    finally:
        cursor.close()
        conn.close()


# Deletes the specified equipment
def delete_equipment(equipment_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        delete_query = sql.SQL("DELETE FROM equipment WHERE equipment_id = %s")
        cursor.execute(delete_query, (equipment_id,))
        conn.commit()
        print("Equipment deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting equipment:", e)
    finally:
        cursor.close()
        conn.close()


# Updates the last time the specified equipment was maintained (sets last maintained to the current date)
def update_equipment_last_maintained(equipment_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        update_query = """
            UPDATE equipment
            SET last_maintained = %s
            WHERE equipment_id = %s
        """

        current_date = date.today()

        cursor.execute(update_query, (current_date, equipment_id))
        conn.commit()
        print("Equipment last maintained date updated successfully.")

    except psycopg2.Error as e:
        print("Error updating equipment last maintained date:", e)
    finally:
        cursor.close()
        conn.close()


# Creates a class run by the specified trainer at the specified time
def create_class(trainer_id, class_date, start_time, end_time):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        insert_query = sql.SQL(
            "INSERT INTO classes (trainer_id, class_date, start_time, end_time) VALUES (%s, %s, %s, %s)")
        cursor.execute(insert_query, (trainer_id, class_date, start_time, end_time))
        conn.commit()
        print("Class created successfully.")
    except psycopg2.Error as e:
        print("Error creating class:", e)
    finally:
        cursor.close()
        conn.close()


# Cancels the specified class
def cancel_class(class_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        delete_query = sql.SQL("DELETE FROM classes WHERE class_id = %s")
        cursor.execute(delete_query, (class_id,))
        conn.commit()
        print("Class canceled successfully.")
    except psycopg2.Error as e:
        print("Error canceling class:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all bills
def view_all_bills():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        select_query = sql.SQL("SELECT * FROM bills")
        cursor.execute(select_query)

        bills = cursor.fetchall()

        print("All Bills:")
        for bill in bills:
            print("Bill ID:", bill[0])
            print("Staff ID:", bill[1])
            print("Member ID:", bill[2])
            print("Bill Date:", bill[3])
            print("Amount:", bill[4])
            print("Paid:", bill[5])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error viewing bills:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all bills assigned to the specified member
def display_bills_by_member_id(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        select_query = """
            SELECT * FROM bills
            WHERE member_id = %s
        """

        cursor.execute(select_query, (member_id,))

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("No bills found for the member.")
        else:
            print("Bills for Member ID:", member_id)
            for row in rows:
                print("Bill ID:", row[0])
                print("Staff ID:", row[1])
                print("Member ID:", row[2])
                print("Bill Date:", row[3])
                print("Amount:", row[4])
                print("Paid:", row[5])
                print("--------------")

    except psycopg2.Error as e:
        print("Error displaying bills:", e)
    finally:
        cursor.close()
        conn.close()


# Creates a bill for the specified member, date and amount
def create_bill(staff_id, member_id, bill_date, amount):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        insert_query = sql.SQL(
            "INSERT INTO bills (staff_id, member_id, bill_date, amount, paid) VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(insert_query, (staff_id, member_id, bill_date, amount, False))
        conn.commit()
        print("Bill created successfully.")
    except psycopg2.Error as e:
        print("Error creating bill:", e)
    finally:
        cursor.close()
        conn.close()


# Deletes the specified bill
def delete_bill(bill_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        delete_query = sql.SQL("DELETE FROM bills WHERE bill_id = %s")
        cursor.execute(delete_query, (bill_id,))
        conn.commit()
        print("Bill deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting bill:", e)
    finally:
        cursor.close()
        conn.close()


def update_bill_staff_id(bill_id, staff_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        update_query = sql.SQL("UPDATE bills SET staff_id = %s WHERE bill_id = %s")
        cursor.execute(update_query, (staff_id, bill_id))
        conn.commit()
        print("Staff ID updated successfully.")
    except psycopg2.Error as e:
        print("Error updating staff ID:", e)
    finally:
        cursor.close()
        conn.close()


def update_bill_member_id(bill_id, member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        update_query = sql.SQL("UPDATE bills SET member_id = %s WHERE bill_id = %s")
        cursor.execute(update_query, (member_id, bill_id))
        conn.commit()
        print("Member ID updated successfully.")
    except psycopg2.Error as e:
        print("Error updating member ID:", e)
    finally:
        cursor.close()
        conn.close()


def update_bill_amount(bill_id, amount):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        update_query = sql.SQL("UPDATE bills SET amount = %s WHERE bill_id = %s")
        cursor.execute(update_query, (amount, bill_id))
        conn.commit()
        print("Amount updated successfully.")
    except psycopg2.Error as e:
        print("Error updating amount:", e)
    finally:
        cursor.close()
        conn.close()


def update_bill_date(bill_id, new_date):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        update_query = sql.SQL("UPDATE bills SET bill_date = %s WHERE bill_id = %s")
        cursor.execute(update_query, (new_date, bill_id))
        conn.commit()
        print("Bill date updated successfully.")
    except psycopg2.Error as e:
        print("Error updating bill date:", e)
    finally:
        cursor.close()
        conn.close()


def update_bill_paid_status(bill_id, paid):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        update_query = sql.SQL("UPDATE bills SET paid = %s WHERE bill_id = %s")
        cursor.execute(update_query, (paid, bill_id))
        conn.commit()
        print("Paid status updated successfully.")
    except psycopg2.Error as e:
        print("Error updating paid status:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all bookings for all trainers
def get_all_bookings():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        select_query = sql.SQL("SELECT * FROM bookings")
        cursor.execute(select_query)

        bookings = cursor.fetchall()

        print("All Bookings:")
        for booking in bookings:
            print("Booking ID:", booking[0])
            print("Trainer ID:", booking[1])
            print("Booking Date:", booking[2])
            print("Booking Start Time:", booking[3])
            print("Booking End Time:", booking[4])
            print("Member ID:", booking[5])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error retrieving bookings:", e)
    finally:
        cursor.close()
        conn.close()


# Displays bookings for the specified member
def display_bookings(member_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT * FROM bookings WHERE member_id = %s
        """)

        cursor.execute(query, (member_id,))
        bookings = cursor.fetchall()

        if bookings:
            print(f"Bookings for Member ID {member_id}:")
            for booking in bookings:
                print(f"Booking ID: {booking[0]}")
                print(f"Trainer ID: {booking[1]}")
                print(f"Booking Date: {booking[2]}")
                print(f"Start Time: {booking[3]}")
                print(f"End Time: {booking[4]}")
                print("------")
        else:
            print("No bookings found for member.")

    except psycopg2.Error as e:
        print("Error displaying bookings:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all bills that have been paid
def get_paid_bills():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        select_query = sql.SQL("SELECT * FROM bills WHERE paid = TRUE")
        cursor.execute(select_query)

        paid_bills = cursor.fetchall()

        print("Paid Bills:")
        for bill in paid_bills:
            print("Bill ID:", bill[0])
            print("Staff ID:", bill[1])
            print("Member ID:", bill[2])
            print("Bill Date:", bill[3])
            print("Amount:", bill[4])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error retrieving paid bills:", e)
    finally:
        cursor.close()
        conn.close()


# Displays all bills that are not yet paid
def display_unpaid_bills():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        select_query = sql.SQL("SELECT * FROM bills WHERE paid = FALSE")
        cursor.execute(select_query)

        unpaid_bills = cursor.fetchall()

        print("Unpaid Bills:")
        for bill in unpaid_bills:
            print("Bill ID:", bill[0])
            print("Staff ID:", bill[1])
            print("Member ID:", bill[2])
            print("Bill Date:", bill[3])
            print("Amount:", bill[4])
            print("-----------------------")

    except psycopg2.Error as e:
        print("Error retrieving unpaid bills:", e)
    finally:
        cursor.close()
        conn.close()


# Returns True if the email already exists in the member system, False if it doesn't
def check_member_email_existence(email):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT EXISTS (
                SELECT 1 FROM members WHERE email = %s
            )
        """)

        cursor.execute(query, (email,))
        exists = cursor.fetchone()[0]

        return exists

    except psycopg2.Error as e:
        print("Error checking member email existence:", e)
        return False
    finally:
        cursor.close()
        conn.close()


# Returns True if the email already exists in the trainer system, False if it doesn't
def check_trainer_email_existence(email):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT EXISTS (
                SELECT 1 FROM trainers WHERE email = %s
            )
        """)

        cursor.execute(query, (email,))
        exists = cursor.fetchone()[0]

        return exists

    except psycopg2.Error as e:
        print("Error checking trainer email existence:", e)
        return False
    finally:
        cursor.close()
        conn.close()


# Returns True if the email already exists in the staff system, False if it doesn't
def check_staff_email_existence(email):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT EXISTS (
                SELECT 1 FROM staff WHERE email = %s
            )
        """)

        cursor.execute(query, (email,))
        exists = cursor.fetchone()[0]

        return exists

    except psycopg2.Error as e:
        print("Error checking staff email existence:", e)
        return False
    finally:
        cursor.close()
        conn.close()


# Checks if the phone number exists in any of the member, trainer or staff systems
def check_phone_existence(phone):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Check phone existence in members table
        check_member_query = sql.SQL("""
            SELECT EXISTS (
                SELECT 1 FROM members WHERE phone = %s
            )
        """)
        cursor.execute(check_member_query, (phone,))
        member_exists = cursor.fetchone()[0]

        # Check phone existence in trainers table
        check_trainer_query = sql.SQL("""
            SELECT EXISTS (
                SELECT 1 FROM trainers WHERE phone = %s
            )
        """)
        cursor.execute(check_trainer_query, (phone,))
        trainer_exists = cursor.fetchone()[0]

        # Return True if phone exists in either table, False otherwise
        return member_exists or trainer_exists

    except psycopg2.Error as e:
        print("Error checking phone existence:", e)
        return None
    finally:
        cursor.close()
        conn.close()


# Returns the id of the member with the specified email
def get_member_id_by_email(email):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Query to get member_id by email
        query = sql.SQL("""
            SELECT member_id FROM members WHERE email = %s
        """)

        cursor.execute(query, (email,))
        result = cursor.fetchone()

        # If result is not None, return member_id, otherwise return None
        return result[0] if result else None

    except psycopg2.Error as e:
        print("Error fetching member_id by email:", e)
        return None
    finally:
        cursor.close()
        conn.close()


# Checks if the email and password given match
def check_credentials(email, password):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Query to check email and password in members table
        query_member = sql.SQL("""
            SELECT EXISTS (
                SELECT 1 FROM members WHERE email = %s AND password = %s
            )
        """)
        cursor.execute(query_member, (email, password))
        member_exists = cursor.fetchone()[0]

        # Query to check email and password in trainers table
        query_trainer = sql.SQL("""
            SELECT EXISTS (
                SELECT 1 FROM trainers WHERE email = %s AND password = %s
            )
        """)
        cursor.execute(query_trainer, (email, password))
        trainer_exists = cursor.fetchone()[0]

        # Query to check email and password in staff table
        query_staff = sql.SQL("""
            SELECT EXISTS (
                SELECT 1 FROM staff WHERE email = %s AND password = %s
            )
        """)
        cursor.execute(query_staff, (email, password))
        staff_exists = cursor.fetchone()[0]

        # Return True if credentials match in any table, otherwise return False
        return member_exists or trainer_exists or staff_exists

    except psycopg2.Error as e:
        print("Error checking credentials:", e)
        return False
    finally:
        cursor.close()
        conn.close()


# Returns the trainer id that corresponds with the specified email
def get_trainer_id_by_email(email):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Query to get trainer_id by email
        query = sql.SQL("""
            SELECT trainer_id FROM trainers WHERE email = %s
        """)

        cursor.execute(query, (email,))
        result = cursor.fetchone()

        # If result is not None, return trainer_id, otherwise return None
        return result[0] if result else None

    except psycopg2.Error as e:
        print("Error fetching trainer_id by email:", e)
        return None
    finally:
        cursor.close()
        conn.close()


# Returns the staff id that corresponds with the specified email
def get_staff_id_by_email(email):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Query to get staff_id by email
        query = sql.SQL("""
            SELECT staff_id FROM staff WHERE email = %s
        """)

        cursor.execute(query, (email,))
        result = cursor.fetchone()

        # If result is not None, return staff_id, otherwise return None
        return result[0] if result else None

    except psycopg2.Error as e:
        print("Error fetching staff_id by email:", e)
        return None
    finally:
        cursor.close()
        conn.close()


# Converts a string into a timestamp
def string_to_timestamp(input_string):
    try:
        timestamp = datetime.strptime(input_string, '%Y-%m-%d %H:%M:%S')
        return timestamp
    except ValueError:
        print("Incorrect format. Please use 'YYYY-MM-DD HH:MM:SS'")
        return None


# The logic that the user goes through when logging in.
def login():
    print("\nWelcome to Sam's Health & Fitness App!")
    choice = input("1 - Login : 2 - Register : 3 - Trainer Login : 4 - Staff Login, Enter to confirm.: ")

    ids = None

    if choice == "1":
        ids = None
        email = input("\nPlease enter your email: ")

        if check_member_email_existence(email) == False:
            print("No account under this email.")
            return None

        password = input("Please enter your password: ")
        if check_credentials(email, password):
            print("Login successful!")
            ids = [get_member_id_by_email(email), 1]
        else:
            print("Wrong password.")
            return None
    elif choice == "2":
        print("\nWelcome! Please enter your information to Register!")
        first = input("Please enter your first name: ")
        last = input("Please enter your last name: ")

        email = input("Please enter your email: ")
        if check_member_email_existence(email):
            print("This email is already in use.")
            return None

        phone = input("Please enter your phone number (XXX-XXX-XXXX): ")
        if check_phone_existence(phone):
            print("This phone number is already in use.")
            return None

        dob = input("Please enter your date of birth (YYYY-MM-DD): ")
        try:
            date_of_birth = datetime.strptime(dob, "%Y-%m-%d").date()
        except:
            print("Invalid date!")
            return None

        join_date = datetime.now().date()
        password = input("Please enter a password: ")
        add_member(first, last, email, phone, date_of_birth, join_date, password)
        add_days_for_member(get_member_id_by_email(email))
        add_health_metrics(get_member_id_by_email(email))

        print("\nThank you for registering!")
        input("You will now be redirected to the Login screen. Press Enter to Continue")
        login()

    elif choice == "3":
        ids = None
        email = input("\nPlease enter your trainer email: ")

        if check_trainer_email_existence(email) == False:
            print("No account under this email.")
            return None

        password = input("Please enter your password: ")
        if check_credentials(email, password):
            print("Login successful!")
            ids = [get_trainer_id_by_email(email), 3]
        else:
            print("Wrong password.")
            return None
    elif choice == "4":
        ids = None
        email = input("\nPlease enter your staff email: ")

        if check_staff_email_existence(email) == False:
            print("No account under this email.")
            return None

        password = input("Please enter your password: ")
        if check_credentials(email, password):
            print("Login successful!")
            ids = [get_staff_id_by_email(email), 4]
        else:
            print("Wrong password.")
            return None
    else:
        print("Invalid Input")
        login()

    return ids


# The member interface
def deal_with_member(id):
    print("\nWelcome!")
    choice = input("1 - Profile : 2 - Dashboard : 3 - Manage Bookings/Classes : 4 - Exit: ")

    if choice == "1":
        display_member(id)
        choice2 = input("1 - Change Profile : 2 - Exit: ")

        if choice2 == "1":
            print("Type the attribute you'd like to change!")
            choice3 = input("(first_name, last_name, email, phone, date_of_birth: ")
            choice4 = input("Please type the new value: ")

            if choice3 == "first_name" or choice3 == "last_name" or choice3 == "email" or choice3 == "phone":
                update_member_attribute(id, choice3, choice4)
                return
            elif choice3 == "date_of_birth":
                update_member_date_of_birth(id, choice4)
                return
            else:
                print("Invalid Input")
        elif choice2 == "2":
            return
        else:
            print("Invalid Input")
            return

    elif choice == "2":
        print("Welcome to the Dashboard!")
        choice2 = input("1 - Health Metrics : 2 - Fitness Goals : 3 - Routines : 4 - Exit: ")

        if choice2 == "1":  # Health metrics
            display_health_metrics(id)
            choice3 = input("1 - Update Health Metrics : 2 - Exit: ")

            if choice3 == "1":
                print("Type the name of the metric you'd like to update!")
                choice4 = input("height_cm, weight_kg, resting_heartrate_bpm, body_fat_percentage: ")
                choice5 = input("Type the new value of the metric: ")
                update_health_metric(id, choice4, choice5)
                return
            elif choice3 == "2":
                return
            else:
                print("Invalid Input")
                return

        elif choice2 == "2":  # fitness goals
            display_goals(id)
            choice3 = input("1 - Add Goal : 2 - Delete Goal : 3 - Exit: ")

            if choice3 == "1":
                choice4 = input("Type the name of the goal you'd like to add!: ")
                add_goal(id, choice4)
                return
            elif choice3 == "2":
                choice4 = input("Type the ID of the goal you'd like to delete!: ")
                if choice4.isdigit():
                    delete_goal(int(choice4))
                else:
                    print("Invalid Input")
                return
            elif choice3 == "3":
                return
            else:
                print("Invalid Input")
                return

        elif choice2 == "3":  # routines
            display_days(id)
            choice3 = input("1 - Add Routine : 2 - Delete Routine : 3 - Exit: ")

            if choice3 == "1":
                choice4 = input("Type the name of the routine you'd like to add!: ")
                choice5 = input("Type the day you'd like to do this routine!: ")
                schedule_routine(id, choice5, choice4)
                return
            elif choice3 == "2":
                choice4 = input("Type the day you'd like to a remove a routine from!: ")
                cancel_routine(id, choice4)
            elif choice3 == "3":
                return
            else:
                print("Invalid Input")
                return

    elif choice == "3":  # manage bookings/classes
        choice2 = input("1 - Bookings : 2 - Classes : 3 - Exit: ")

        if choice2 == "1":
            display_bookings(id)
            choice3 = input("1 - View Available Times : 2 - Book Trainer : 3 - Cancel Booking : 4 - Exit: ")

            if choice3 == "1":
                view_available_bookings()
                return

            elif choice3 == "2":
                choice4 = input("Type the ID of the timeslot you'd like to book!: ")
                if choice4.isdigit():
                    book_with_trainer(id, int(choice4))
                else:
                    print("Invalid Input")
                return

            elif choice3 == "3":
                choice4 = input("Type the ID of the timeslot you'd like to cancel!: ")
                if choice4.isdigit():
                    cancel_trainer(int(choice4))
                else:
                    print("Invalid Input")
                return
            else:
                print("Invalid Input")
                return

        elif choice2 == "2":
            view_enrolled_classes(id)
            choice3 = input("1 - View Available Classes : 2 - Join Class : 3 - Leave Class : 4 - Exit: ")

            if choice3 == "1":
                display_all_classes()
                return

            elif choice3 == "2":
                choice4 = input("Type the ID of the class you'd like to join!: ")
                if choice4.isdigit():
                    enroll_in_class(id, int(choice4))
                else:
                    print("Invalid Input")
                return

            elif choice3 == "3":
                choice4 = input("Type the ID of the class you'd like to leave!: ")
                if choice4.isdigit():
                    leave_class(id, int(choice4))
                else:
                    print("Invalid Input")
                return

            elif choice3 == "4":
                return
            else:
                print("Invalid Input")
                return

        elif choice2 == "3":
            return
        else:
            print("Invalid Input")
            return

    elif choice == "4":
        quit()

    else:
        print("Invalid Input")
        return


# The trainer interface
def deal_with_trainer(id):
    print("\nWelcome!")
    choice = input("1 - Bookings : 2 - Members : 3 - Exit: ")

    if choice == "1":
        get_bookings(id)
        choice2 = input("1 - Add New Booking : 2 - Delete Booking : 3 - Exit: ")

        if choice2 == "1":
            choice3 = datetime.strptime(input("Type the date of the booking! (YYYY-MM-DD): "), "%Y-%m-%d").date()
            choice4 = string_to_timestamp(input("Type the start time (YYYY-MM-DD HH:MM:SS): "))
            choice5 = string_to_timestamp(input("Type the end time (YYYY-MM-DD HH:MM:SS): "))
            add_booking(id, choice3, choice4, choice5)
            return

        elif choice2 == "2":
            choice3 = input("Type the ID of the booking you'd like to delete:  ")
            if choice3.isdigit():
                remove_booking(int(choice3))
            else:
                print("Invalid Input")
            return

        elif choice2 == "3":
            return
        else:
            print("Invalid Input")
            return

    elif choice == "2":
        choice2 = input("1 - View All Members : 2 - Search Member : 3 - Exit:  ")

        if choice2 == "1":
            get_all_members()
            return
        elif choice2 == "2":
            choice3 = input("Type the ID of the member you'd like to search!: ")
            if choice3.isdigit():
                display_member(int(choice3))
            else:
                print("Invalid Input")
            return
        elif choice2 == "3":
            return
        else:
            print("Invalid Input")
            return

    elif choice == "3":
        quit()

    else:
        print("Invalid Input")
        return


# The staff interface
def deal_with_staff(id):
    print("\nWelcome!")
    choice = input("1 - Equipment : 2 - Classes : 3 - Trainers : 4 - Bills : 5 - Exit: ")

    if choice == "1":
        get_all_equipment()
        choice2 = input("1 - Update Maintenance : 2 - Add Equipment : 3 - Delete Equipment : 4 - Exit: ")

        if choice2 == "1":
            choice3 = input("Type the ID of the equipment you'd like to update maintenance for: ")
            if choice3.isdigit():
                update_equipment_last_maintained(int(choice3))
            else:
                print("Invalid Input")
            return
        elif choice2 == "2":
            choice3 = input("Type the name of the new piece of equipment!: ")
            add_equipment(choice3, datetime.now())
            return
        elif choice2 == "3":
            choice3 = input("Type the ID of the equipment to delete: ")
            if choice3.isdigit():
                delete_equipment(int(choice3))
            else:
                print("Invalid Input")
        elif choice2 == "4":
            return
        else:
            print("Invalid Input")
            return

    elif choice == "2":
        display_all_classes()
        choice2 = input("1 - Create Class : 2 - Cancel Class : 3 - Exit: ")

        if choice2 == "1":
            choice3 = datetime.strptime(input("Type the date of the class! (YYYY-MM-DD): "), "%Y-%m-%d").date()
            choice4 = string_to_timestamp(input("Type the start time (YYYY-MM-DD HH:MM:SS): "))
            choice5 = string_to_timestamp(input("Type the end time (YYYY-MM-DD HH:MM:SS): "))
            choice6 = input("Type the ID of the trainer who will lead this class!: ")
            if choice6.isdigit():
                create_class(int(choice6), choice3, choice4, choice5)
            else:
                print("Invalid Input")
            return
        elif choice2 == "2":
            choice3 = input("Type the class ID of the class you'd like to delete: ")
            if choice3.isdigit():
                cancel_class(int(choice3))
            else:
                print("Invalid Input")
            return
        elif choice2 == "3":
            return
        else:
            print("Invalid Input")
            return

    elif choice == "3":
        get_all_trainers()
        choice2 = input("1 - Add Trainer : 2 - Delete Trainer : 3 - Exit: ")

        if choice2 == "1":
            choice3 = input("Type the first name of the trainer you'd like to add: ")
            choice4 = input("Type the last name of the trainer you'd like to add: ")
            choice5 = input("Type the email of the trainer you'd like to add: ")
            choice6 = input("Type the phone of the trainer you'd like to add: ")
            choice7 = input("Type a password for the trainer you'd like to add: ")
            add_trainer(choice3, choice4, choice5, choice6, choice7)
            return
        elif choice2 == "2":
            choice3 = input("Type the ID of the trainer you'd like to delete: ")
            if choice3.isdigit():
                delete_trainer(int(choice3))
            else:
                print("Invalid Input")
            return
        elif choice2 == "3":
            return
        else:
            print("Invalid Input")
            return

    elif choice == "4":
        choice2 = input("1 - Search Bills : 2 - Create Bill : 3 - Delete Bill : 4 - Pay Bill : 5 - Exit: ")

        if choice2 == "1":
            choice3 = input("1 - Unpaid Bills : 2 - Paid Bills : 3 - Search by Member : 4 - Exit: ")

            if choice3 == "1":
                display_unpaid_bills()
                return
            elif choice3 == "2":
                get_paid_bills()
                return
            elif choice3 == "3":
                choice4 = input("Type the ID of the member to search for: ")
                if choice4.isdigit():
                    display_bills_by_member_id(int(choice4))
                else:
                    print("Invalid Input")
                return
            elif choice3 == "4":
                choice4 = input("Type the ID of the bill to pay: ")
                if choice4.isdigit():
                    update_bill_paid_status(int(choice4), True)
                else:
                    print("Invalid Input")
            elif choice3 == "5":
                return
            else:
                print("Invalid Input")
                return

        elif choice2 == "2":
            choice3 = input("Type the ID of the member to bill: ")
            choice4 = input("Type the cent amount for the bill ")
            if choice3.isdigit():
                create_bill(id, int(choice3), datetime.now(), int(choice4))
            else:
                print("Invalid Input")
            return

        elif choice2 == "3":
            choice3 = input("Type the ID of the bill to delete: ")
            if choice3.isdigit():
                delete_bill(int(choice3))
            else:
                print("Invalid Input")
            return

        elif choice2 == "4":
            return
        else:
            print("Invalid Input")
            return

    elif choice == "5":
        quit()
    else:
        print("Invalid Input")
        return


if __name__ == "__main__":

    rank = None
    ids = None
    id = None

    while ids == None:
        ids = login()

    id = ids[0]
    rank = ids[1]

    if rank == 1:
        while (True):
            deal_with_member(id)
    elif rank == 3:
        while (True):
            deal_with_trainer(id)
    elif rank == 4:
        while (True):
            deal_with_staff(id)
    else:
        print("Oops! Something went wrong.")
        quit()

