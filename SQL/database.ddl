-- Create Members Table
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    phone VARCHAR NOT NULL UNIQUE,
    date_of_birth DATE,
    join_date DATE,
    password VARCHAR NOT NULL
);

-- Create Trainers Table
CREATE TABLE trainers (
    trainer_id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    phone VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL
);

-- Create Staff Table
CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    phone VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL
);

-- Create Health Metrics Table
CREATE TABLE health_metrics (
    member_id INTEGER PRIMARY KEY REFERENCES members(member_id),
    height_cm INTEGER,
    weight_kg INTEGER,
    resting_heartrate_bpm INTEGER,
    body_fat_percentage INTEGER
);

-- Create Classes Table
CREATE TABLE classes (
    class_id SERIAL PRIMARY KEY,
    trainer_id INTEGER NOT NULL REFERENCES trainers(trainer_id),
    class_date DATE NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL
);

-- Create Goals Table
CREATE TABLE goals (
    goal_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id),
    goal TEXT
);

-- Create Bills Table
CREATE TABLE bills (
    bill_id SERIAL PRIMARY KEY,
    staff_id INTEGER NOT NULL REFERENCES staff(staff_id),
    member_id INTEGER NOT NULL REFERENCES members(member_id),
    bill_date DATE NOT NULL,
    amount INTEGER NOT NULL,
    paid BOOLEAN NOT NULL
);

-- Create Routines Table
CREATE TABLE routines (
    routine_id SERIAL PRIMARY KEY,
    routine_name VARCHAR NOT NULL,
    member_id INTEGER NOT NULL REFERENCES members(member_id)
);

-- Create Days Table
CREATE TABLE days (
    day VARCHAR,
    member_id INTEGER NOT NULL REFERENCES members(member_id),
    routine_id INTEGER REFERENCES routines(routine_id)
);

-- Create Equipment Table
CREATE TABLE equipment (
    equipment_id SERIAL PRIMARY KEY,
    equipment_name VARCHAR NOT NULL,
    last_maintained DATE NOT NULL
);

-- Create Bookings Table
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    trainer_id INTEGER NOT NULL REFERENCES trainers(trainer_id),
    booking_date DATE NOT NULL,
    booking_start TIMESTAMP NOT NULL,
    booking_end TIMESTAMP NOT NULL,
    member_id INTEGER REFERENCES members(member_id)
);

-- Create Class Enrollments Table
CREATE TABLE class_enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    class_id INTEGER NOT NULL REFERENCES classes(class_id),
    member_id INTEGER NOT NULL REFERENCES members(member_id)
);
