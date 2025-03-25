import sqlite3

# Step 1: Create SQLite Database and Tables
db_path = "employee_management0.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create Tables

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    EmpID INTEGER PRIMARY KEY,
    Name TEXT,
    DeptID INTEGER,
    PositionID INTEGER,
    HireDate TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments (
    DeptID INTEGER PRIMARY KEY,
    DeptName TEXT,
    FOREIGN KEY (DeptID) REFERENCES Employees(DeptID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Positions (
    PositionID INTEGER PRIMARY KEY,
    Position_Name ,
    FOREIGN KEY (PositionID) REFERENCES Employees(PositionID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Salaries (
    SalaryID INTEGER PRIMARY KEY,
    EmpID INTEGER,
    Amount REAL,
    PayDate TEXT,
    FOREIGN KEY (EmpID) REFERENCES Employees(EmpID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Benefits (
    BenefitID INTEGER PRIMARY KEY,
    EmpID INTEGER,
    BenefitType TEXT,
    StartDate TEXT,
    FOREIGN KEY (EmpID) REFERENCES Employees(EmpID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Projects (
    ProjectID INTEGER PRIMARY KEY,
    EmpID INTEGER,
    Name TEXT,
    Budget REAL,
    FOREIGN KEY (EmpID) REFERENCES Employees(EmpID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clients (
    ClientID INTEGER PRIMARY KEY,
    ProjectID INTEGER,
    Name TEXT,
    DeptID INTEGER,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
)
""")

# Commit changes and close connection
conn.commit()
conn.close()

#Connect to SQLlite database

conn = sqlite3.connect("employee_management0.db")
cursor = conn.cursor()

# Insert data into tables

#Insert into Deoartments table
Dep = [
    (1, "HR"),
    (2, "IT"),
    (3, "Finance")
    ]
cursor.executemany("INSERT INTO Departments VALUES (?, ?)", Dep)

#Insert into Positions table
Pos  = [
    (1, "Manager"),
    (2, "Software Engineer"),
    (3, "Sales Executive")
    ]
cursor.executemany("INSERT INTO Positions VALUES (?, ?)", Pos)

# Insert into Salaries table
Sal = [
    (1, 1, 5000, "2021-01-01"),
    (2, 2, 3000, "2021-01-01"),
    (3, 3, 2000, "2021-01-01")
]
cursor.executemany("INSERT INTO Salaries VALUES (?, ?, ?, ?)", Sal)

#Insert into Employees table
Emp = [
    (1, "John Doe", 1, 1, "2021-01-01"),
    (2, "Jane Doe", 2, 2, "2021-01-01"),
    (3, "Alice Smith", 3, 3, "2021-01-01")
    ]
cursor.executemany("INSERT INTO Employees VALUES (?, ?, ?, ?, ?)", Emp)

#Insert into Benefits table

Ben = [
    (1, 1, "Health Insurance", "2021-01-01"),
    (2, 2, "Dental Insurance", "2021-01-01"),
    (3, 3, "Vision Insurance", "2021-01-01")
    ]
cursor.executemany("INSERT INTO Benefits VALUES (?, ?, ?, ?)", Ben)

#Insert into Projects table
Pro = [
    (1, 1, "Project A", 10000),
    (2, 2, "Project B", 20000),
    (3, 3, "Project C", 30000)
    ]
cursor.executemany("INSERT INTO Projects VALUES (?, ?, ?, ?)", Pro)

#Insert into Clients table
Cli = [
    (1, 1, "Client A", 1),
    (2, 2, "Client B", 2),
    (3, 3, "Client C", 3)
    ]
cursor.executemany("INSERT INTO Clients VALUES (?, ?, ?, ?)", Cli)

conn.commit()
conn.close()
