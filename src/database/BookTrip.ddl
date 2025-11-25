CREATE TABLE connection (
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

CREATE TABLE trip (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_code TEXT GENERATED ALWAYS AS ('A' || id) VIRTUAL,
    status VARCHAR (50),
    directConnectionID INTEGER NOT NULL,
    multiStopConnectionID INTEGER,
    FOREIGN KEY (directConnectionID) REFERENCES connection (route_id),
    FOREIGN KEY (multiStopConnectionID) REFERENCES connection (route_id)
);


CREATE TABLE traveler (
    travelerId INTEGER PRIMARY KEY AUTOINCREMENT ,
    travelerFName TEXT NOT NULL,
    travelerLName VARCHAR(50) NOT NULL,
    travelerAge VARCHAR(50) NOT NULL
);

CREATE TABLE ticket (
    id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE reservation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    travelerId INTEGER NOT NULL,
    ticketId INTEGER NOT NULL,
    tripID INTEGER NOT NULL,
    FOREIGN KEY (tripID) REFERENCES trip (id),
    FOREIGN KEY (travelerId) REFERENCES traveler (travelerId),
    FOREIGN KEY (ticketId) REFERENCES ticket (id),
    UNIQUE (travelerId,tripID)
);

CREATE TABLE trip_catalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tripId INTEGER NOT NULL,
    FOREIGN KEY (tripId) REFERENCES trip (id)
);

CREATE TABLE ticket_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticketId INTEGER,
    FOREIGN KEY (ticketId) REFERENCES ticket (id)
);

CREATE TABLE traveler_catalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    travelerId INTEGER,
    FOREIGN KEY (travelerId) REFERENCES traveler (travelerId)
);