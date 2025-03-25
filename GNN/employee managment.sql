create database EmployeeManagement;

use EmployeeManagement;

-- Departments Table
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- Positions Table
CREATE TABLE Positions (
    position_id INT PRIMARY KEY,
    position_name VARCHAR(50)
);

-- Salaries Table
CREATE TABLE Salaries (
    salary_id INT PRIMARY KEY,
    amount DECIMAL(10, 2),
    salary_date DATE
);

-- Employees Table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    hire_date DATE,
    department_id INT,
    position_id INT,
    salary_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id),
    FOREIGN KEY (position_id) REFERENCES Positions(position_id),
    FOREIGN KEY (salary_id) REFERENCES Salaries(salary_id)
);

-- Benefits Table
CREATE TABLE Benefits (
    benefit_id INT PRIMARY KEY,
    benefit_name VARCHAR(50),
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

-- Projects Table
CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    employee_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

-- EmployeeTraining Table
CREATE TABLE EmployeeTraining (
    training_id INT PRIMARY KEY,
    training_name VARCHAR(100),
    training_date DATE,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

-- Sample Data for Departments Table
INSERT INTO Departments (department_id, department_name)
VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Sales');

-- Sample Data for Positions Table
INSERT INTO Positions (position_id, position_name)
VALUES
(1, 'HR Manager'),
(2, 'Software Engineer'),
(3, 'Sales Executive');

-- Sample Data for Salaries Table
INSERT INTO Salaries (salary_id, amount, salary_date)
VALUES
(1, 60000.00, '2023-01-01'),
(2, 85000.00, '2023-01-01'),
(3, 50000.00, '2023-01-01');

-- Sample Data for Employees Table
INSERT INTO Employees (employee_id, first_name, last_name, date_of_birth, hire_date, department_id, position_id, salary_id)
VALUES
(1, 'John', 'Doe', '1985-05-15', '2020-01-10', 1, 2, 1),
(2, 'Jane', 'Smith', '1990-07-22', '2019-03-05', 2, 3, 2),
(3, 'Emily', 'Jones', '1987-11-30', '2021-06-20', 3, 1, 3);

-- Sample Data for Benefits Table
INSERT INTO Benefits (benefit_id, benefit_name, employee_id)
VALUES
(1, 'Health Insurance', 1),
(2, 'Retirement Plan', 2),
(3, 'Paid Time Off', 3);

-- Sample Data for Projects Table
INSERT INTO Projects (project_id, project_name, employee_id, start_date, end_date)
VALUES
(1, 'Employee Portal', 1, '2023-02-01', '2023-12-31'),
(2, 'Website Redesign', 2, '2023-03-15', '2024-05-30'),
(3, 'Sales Strategy', 3, '2023-05-10', '2024-01-15');

-- Sample Data for EmployeeTraining Table
INSERT INTO EmployeeTraining (training_id, training_name, training_date, employee_id)
VALUES
(1, 'Leadership Development', '2023-04-10', 1),
(2, 'Advanced Java Programming', '2023-07-20', 2),
(3, 'Sales Skills Workshop', '2023-08-05', 3);

