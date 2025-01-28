import sqlite3

conn = sqlite3.connect("colonial_adventure_tours.db")
cursor = conn.cursor()

# Participants Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Participants (
    ParticipantNumber INTEGER PRIMARY KEY,
    LastName TEXT NOT NULL,
    FirstName TEXT NOT NULL,
    Address TEXT,
    City TEXT,
    State TEXT,
    PostalCode TEXT,
    TelephoneNumber TEXT,
    DateOfBirth DATE
);
""")

# AdventureClasses Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS AdventureClasses (
    ClassNumber INTEGER PRIMARY KEY,
    ClassDescription TEXT NOT NULL,
    MaxParticipants INTEGER NOT NULL,
    ClassFee REAL NOT NULL
);
""")

# Enrollments Table (for many-to-many relationship)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollments (
    EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    ParticipantNumber INTEGER NOT NULL,
    ClassNumber INTEGER NOT NULL,
    ClassDate DATE NOT NULL,
    FOREIGN KEY (ParticipantNumber) REFERENCES Participants(ParticipantNumber),
    FOREIGN KEY (ClassNumber) REFERENCES AdventureClasses(ClassNumber)
);
""")

conn.commit()

# a) Participant Details
query_participant_details = """
SELECT 
    ParticipantNumber, 
    LastName, 
    FirstName, 
    Address, 
    City, 
    State, 
    PostalCode, 
    TelephoneNumber, 
    DateOfBirth
FROM 
    Participants;
"""

# b) Adventure Class Details
query_adventure_class_details = """
SELECT 
    ClassNumber, 
    ClassDescription, 
    MaxParticipants, 
    ClassFee
FROM 
    AdventureClasses;
"""

# c) Participant and Class Enrollment Details
query_participant_enrollments = """
SELECT 
    P.ParticipantNumber, 
    P.LastName, 
    P.FirstName, 
    E.ClassNumber, 
    C.ClassDescription, 
    E.ClassDate
FROM 
    Participants P
JOIN 
    Enrollments E ON P.ParticipantNumber = E.ParticipantNumber
JOIN 
    AdventureClasses C ON E.ClassNumber = C.ClassNumber;
"""

# d) Class and Participant Enrollment Details
query_class_enrollments = """
SELECT 
    E.ClassDate, 
    C.ClassNumber, 
    C.ClassDescription, 
    P.ParticipantNumber, 
    P.LastName, 
    P.FirstName
FROM 
    AdventureClasses C
JOIN 
    Enrollments E ON C.ClassNumber = E.ClassNumber
JOIN 
    Participants P ON E.ParticipantNumber = P.ParticipantNumber;
"""

conn.close()
