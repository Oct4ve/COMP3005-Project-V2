-- Populate Trainers
INSERT INTO trainers (first_name, last_name, email, phone, password)
VALUES
    ('Mike', 'Johnson', 'mike.johnson@example.com', '1111111111', 'trainerpass1'),
    ('Sarah', 'Williams', 'sarah.williams@example.com', '2222222222', 'trainerpass2'),
    ('David', 'Taylor', 'david.taylor@example.com', '3333333333', 'trainerpass3');

-- Populate Staff
INSERT INTO staff (first_name, last_name, email, phone, password)
VALUES
    ('Anna', 'Davis', 'anna.davis@example.com', '4444444444', 'staffpass1'),
    ('James', 'Martinez', 'james.martinez@example.com', '5555555555', 'staffpass2'),
    ('Laura', 'Jones', 'laura.jones@example.com', '6666666666', 'staffpass3');

-- Populate classes
INSERT INTO classes (trainer_id, class_date, start_time, end_time)
VALUES 
    (1, '2024-04-15', TIMESTAMP '2024-04-15 10:00:00', TIMESTAMP '2024-04-15 11:00:00'),
    (1, '2024-04-16', TIMESTAMP '2024-04-16 14:00:00', TIMESTAMP '2024-04-16 15:00:00'),
    (2, '2024-04-17', TIMESTAMP '2024-04-17 09:30:00', TIMESTAMP '2024-04-17 10:30:00'),
    (2, '2024-04-18', TIMESTAMP '2024-04-18 16:00:00', TIMESTAMP '2024-04-18 17:00:00'),
    (3, '2024-04-19', TIMESTAMP '2024-04-19 11:00:00', TIMESTAMP '2024-04-19 12:00:00');

-- Populate Equipment
INSERT INTO equipment (equipment_name, last_maintained)
VALUES
    ('Treadmill', '2024-03-01'),
    ('Dumbbells', '2024-02-15'),
    ('Yoga Mat', '2024-01-20');
