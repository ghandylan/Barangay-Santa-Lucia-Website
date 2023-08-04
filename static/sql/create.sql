drop database if exists barangay_db;
create database if not exists barangay_db;
use barangay_db;

CREATE TABLE Photo
(
    id        int          NOT NULL AUTO_INCREMENT primary key,
    file_name varchar(255) NOT NULL,
    data      longblob     NOT NULL,
    owner_id  VARCHAR(255) NOT NULL
);

CREATE TABLE Resident
(
    id              VARCHAR(255) PRIMARY KEY,
    photo           int,
    full_name       VARCHAR(255),
    sex             VARCHAR(50),
    username        VARCHAR(50),
    password        VARCHAR(50),
    birthdate       VARCHAR(50),
    relocation_year VARCHAR(50),
    address         VARCHAR(255),

    FOREIGN KEY (photo) REFERENCES Photo (id)
);

ALTER TABLE Photo
    ADD FOREIGN KEY (owner_id) REFERENCES Resident (id);


CREATE TABLE Barangay_Official
(
    id              VARCHAR(255) PRIMARY KEY,

    photo           int,
    full_name       VARCHAR(255),
    sex             VARCHAR(50),
    username        VARCHAR(50),
    password        VARCHAR(50),

    birthdate       VARCHAR(50),
    relocation_year VARCHAR(50),
    address         VARCHAR(255),

    FOREIGN KEY (photo) REFERENCES Photo (id)
);



CREATE TABLE Maligaya_Court_Reservation_List
(
    id                  INTEGER PRIMARY KEY AUTO_INCREMENT,

    full_name           VARCHAR(255),
    purpose             VARCHAR(255),
    number_of_attendees INTEGER,

    reservation_date    VARCHAR(255),
    reservation_time    VARCHAR(255),

    resident_id         VARCHAR(255),

    FOREIGN KEY (resident_id) REFERENCES Resident (id)
);

CREATE TABLE Countryside_Court_Reservation_List
(
    id                  INTEGER PRIMARY KEY AUTO_INCREMENT,

    full_name           VARCHAR(255),
    purpose             VARCHAR(255),
    number_of_attendees INTEGER,

    reservation_date    VARCHAR(255),
    reservation_time    VARCHAR(255),

    resident_id         VARCHAR(255),

    FOREIGN KEY (resident_id) REFERENCES Resident (id)
);

CREATE TABLE Tennis_Court_Reservation_List
(
    id                  INTEGER PRIMARY KEY AUTO_INCREMENT,

    full_name           VARCHAR(255),
    purpose             VARCHAR(255),
    number_of_attendees INTEGER,

    reservation_date    VARCHAR(255),
    reservation_time    VARCHAR(255),

    resident_id         VARCHAR(255),

    FOREIGN KEY (resident_id) REFERENCES Resident (id)
);

CREATE TABLE Items
(
    id            INTEGER PRIMARY KEY AUTO_INCREMENT,
    item_name     VARCHAR(255),
    item_quantity INTEGER
);


CREATE TABLE Item_Rentals
(
    id              int          NOT NULL AUTO_INCREMENT primary key,
    resident_id     VARCHAR(255) NOT NULL,

    chairs_borrowed int          NOT NULL,
    tables_borrowed int          NOT NULL,
    tents_borrowed  int          NOT NULL,

    borrow_date     date         NOT NULL,

    FOREIGN KEY (resident_id) REFERENCES resident (id)
);

INSERT INTO items (item_name, item_quantity)
VALUES ('Chairs', 100),
       ('Tables', 50),
       ('Tents', 25);

# for debugging only
INSERT INTO barangay_official(id, photo, full_name, sex, username, password, birthdate, relocation_year,
                              address)

VALUES (UUID(),
        null,
        'Dylan Louis Tayag',
        'Male',
        'ghandylan',
        'password',
        '1999-09-09',
        '2000',
        'Brgy. Maligaya, San Jose City, Nueva Ecija');

