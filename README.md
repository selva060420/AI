-- Step 1: Create the database
CREATE DATABASE college;

-- Step 2: Use the database
USE college;

-- Step 3: Create a table to store student data
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    grade INT,
    maths_marks INT,
    science_marks INT,
    english_marks INT
);

-- Step 4: Insert 10 student records
INSERT INTO students (name, age, grade, maths_marks, science_marks, english_marks)
VALUES
('Anita', 19, 85, 95, 80, 70),
('Bala', 20, 78, 88, 75, 70),
('Chitra', 18, 92, 100, 85, 90),
('Dinesh', 21, 64, 70, 60, 62),
('Elango', 19, 23, 25, 20, 24),
('Farah', 22, 81, 79, 84, 80),
('Ganesh', 18, 97, 100, 95, 96),
('Hema', 19, 45, 48, 42, 46),
('Irfan', 20, 19, 15, 20, 22),
('Jaya', 18, 88, 90, 85, 88);

-- Step 5: Select all students
SELECT * FROM students;

-- Step 6: Select students with grade above 80
SELECT * FROM students WHERE grade > 80;

-- Step 7: Select students with grade below 25
SELECT * FROM students WHERE grade < 25;

-- Step 8: Select students who got 100% in Maths
SELECT * FROM students WHERE maths_marks = 100;
