import sqlite3

#Initializes the tables and data
def makeDatabase():
    conn = sqlite3.connect('Solmaris.db')
    cursor = conn.cursor()

    #Creation of renter Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS renter (
        number INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        middleInitial TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        postalCode TEXT NOT NULL,
        telephoneNumber TEXT NOT NULL,
        emailAddress TEXT NOT NULL
    )
    ''')

    renterData = [
                    (1, "Fname", "Lname", "X", "December Ave.", "Itchyworms", "Solid", "911", "043-3333", "@gmail.com"),
                    (2, "Fname", "Lname", "X", "December Ave.", "Itchyworms", "Liquid", "911", "043-3333", "@outlook.com"),
                    (3, "Fname", "Lname", "X", "December Ave.", "Itchyworms", "Gas", "911", "043-3333", "@mymail.mapua.edu.ph"),
                    (4, "Fname", "Lname", "X", "December Ave.", "Itchyworms", "Plasma", "911", "043-3333", "@dlsl.edu.ph")
                    ]

    cursor.executemany('''
    INSERT INTO renter (number ,firstName, lastName, middleInitial, address, city, state, postalCode, telephoneNumber, emailAddress) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', renterData)

    conn.commit()

    #Creation of property Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS property (
        locationNumber INTEGER PRIMARY KEY,
        locationName TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        postalCode TEXT NOT NULL,
        unitNumber TEXT NOT NULL,
        squareFootage TEXT NOT NULL,
        NumberOfBedrooms TEXT NOT NULL,
        NumberOfBathrooms TEXT NOT NULL,
        maxRenters TEXT NOT NULL,
        weeklyRate FLOAT NOT NULL  
    )
    ''')

    propertyData = [
                    (1, "locName", "December Ave.", "Itchyworms", "Solid", "420", "69", "69420sq ft", 1, 1, 3, 33.33),
                    (2, "locName", "December Ave.", "Itchyworms", "Liquid", "420", "69", "69420sq ft", 1, 1, 2, 33.33),
                    (3, "locName", "December Ave.", "Itchyworms", "Gas", "420", "69", "69420sq ft", 1, 1, 1, 33.33),
                    (4, "locName", "December Ave.", "Itchyworms", "Plasma", "420", "69", "69420sq ft", 1, 1, 0, 33.33)
                    ]

    cursor.executemany('''
    INSERT INTO property (locationNumber ,locationName, address, city, state, postalCode, unitNumber, squareFootage, NumberOfBedrooms, NumberOfBathrooms, maxRenters, weeklyRate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', propertyData)

    conn.commit()

#Creation of rentalAgreement Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rentalAgreement (
        renterNumber INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        middleInitial TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        postalCode TEXT NOT NULL,
        telephoneNumber TEXT NOT NULL,
        startDate TEXT NOT NULL,
        endDate TEXT NOT NULL,
        weeklyRental FLOAT NOT NULL,
        rentalPeriod FLOAT NOT NULL
    )
    ''')

    rentalAgreementData = [
                    (1, "Fname", "Lname", "X", "December Ave.", "Itchyworms", "Solid", "911", "043-3333", "01/11/1111", "01/11/2222", 33.33, 44.3),
                    (2, "Fname", "Lname", "X", "December Ave.", "Itchyworms", "Liquid", "911", "043-3333", "01/11/1111", "01/11/2222", 33.33, 44.3),
                    (3, "Fname", "Lname", "X", "December Ave.", "Itchyworms", "Gas", "911", "043-3333", "01/11/1111", "01/11/2222", 33.33, 44.3),
                    (4, "Fname", "Lname", "X", "December Ave.", "Itchyworms", "Plasma", "911", "043-3333", "01/11/1111", "01/11/2222", 33.33, 44.3)
                    ]

    cursor.executemany('''
    INSERT INTO rentalAgreement (renterNumber ,firstName, lastName, middleInitial, address, city, state, postalCode, telephoneNumber, startDate, endDate, weeklyRental, rentalPeriod) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', rentalAgreementData)

    conn.commit()
 
    conn.close()

#Defining print function
def printTables():
    conn = sqlite3.connect('Solmaris.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM renter')
    rows = cursor.fetchall()

    print("Renter Table:")
    for row in rows:
        print(row)

    cursor.execute('SELECT * FROM property')
    rows = cursor.fetchall()

    print("Property Table:")
    for row in rows:
        print(row)

    cursor.execute('SELECT * FROM rentalAgreement')
    rows = cursor.fetchall()

    print("Rental Agreement Table:")
    for row in rows:
        print(row)

    conn.close()

printTables()