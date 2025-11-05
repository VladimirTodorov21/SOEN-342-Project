CREATE TABLE soen342project.connection (
    route_id INT PRIMARY KEY,
    departure_city VARCHAR(50) NOT NULL,
    arrival_city VARCHAR(50) NOT NULL,
    departure_time VARCHAR(50) NOT NULL,
    arrival_time VARCHAR(50) NOT NULL,
    train_type VARCHAR(50) NOT NULL,
    days_of_operation VARCHAR(50) NOT NULL,
    first_class_price INT NOT NULL,
    second_class_price INT NOT NULL
);

CREATE TABLE soen342project.trip (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_code TEXT GENERATED ALWAYS AS ('A' || id) VIRTUAL,
    status VARCHAR (50),
    directConnectionID INT NOT NULL,
    multiStopConnectionID INT,
    FOREIGN KEY (directConnectionID) REFERENCES connection (route_id),
    FOREIGN KEY (multiStopConnectionID) REFERENCES connection (route_id)
);

CREATE TABLE soen342project.reservation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    travelerId INTEGER,
    ticketId INTEGER,
    tripID INTEGER,
    FOREIGN KEY (tripID) REFERENCES trip (tripId)
    FOREIGN KEY (travelerId) REFERENCES traveler (travelerId),
    FOREIGN KEY (ticketId) REFERENCES ticket (id)
);

CREATE TABLE soen342project.traveler (
    travelerId INTEGER PRIMARY KEY ,
    travelerLName VARCHAR(50) NOT NULL,
    travelerAge VARCHAR(50) NOT NULL,
    FOREIGN KEY (reservationId) REFERENCES reservation (id)
);

CREATE TABLE soen342project.ticket (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reservationId INTEGER,
    FOREIGN KEY (reservationId) REFERENCES reservation (ID)
);

CREATE TABLE soen342project.trip_catalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tripId INTEGER,
    FOREIGN KEY (tripId) REFERENCES trip (id)
);

CREATE TABLE soen342project.ticket_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticketId INTEGER,
    FOREIGN KEY (ticketId) REFERENCES ticket (id)
);

CREATE TABLE soen342project.traveler_catalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    travelerId INTEGER,
    FOREIGN KEY (travelerId) REFERENCES traveler (travelerId)
);