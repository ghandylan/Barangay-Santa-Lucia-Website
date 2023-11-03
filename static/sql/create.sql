drop database if exists barangay_db;
create database if not exists barangay_db;
use barangay_db;

CREATE TABLE photo
(
    id        int          NOT NULL AUTO_INCREMENT primary key,
    file_name varchar(255) NOT NULL,
    data      longblob     NOT NULL,
    owner_id  VARCHAR(255) NOT NULL
);

CREATE TABLE resident
(
    id              VARCHAR(255) PRIMARY KEY,
    role            VARCHAR(255),
    photo           int,

    full_name       VARCHAR(255),
    sex             VARCHAR(50),
    username        VARCHAR(50),
    password        VARCHAR(50),
    birthdate       VARCHAR(50),
    relocation_year VARCHAR(50),
    address         VARCHAR(255),

    FOREIGN KEY (photo) REFERENCES photo (id)
);

ALTER TABLE photo
    ADD FOREIGN KEY (owner_id) REFERENCES resident (id);


CREATE TABLE barangay_official
(
    id              VARCHAR(255) PRIMARY KEY,
    role            VARCHAR(255),
    photo           int,

    full_name       VARCHAR(255),
    sex             VARCHAR(50),
    username        VARCHAR(50),
    password        VARCHAR(50),
    birthdate       VARCHAR(50),
    relocation_year VARCHAR(50),
    address         VARCHAR(255),

    FOREIGN KEY (photo) REFERENCES photo (id)
);



CREATE TABLE maligaya_court_reservation_list
(
    id                  INTEGER PRIMARY KEY AUTO_INCREMENT,

    full_name           VARCHAR(255),
    purpose             VARCHAR(255),
    number_of_attendees INTEGER,

    reservation_date    VARCHAR(255),
    reservation_time    VARCHAR(255),

    resident_id         VARCHAR(255),

    FOREIGN KEY (resident_id) REFERENCES resident (id)
);

CREATE TABLE countryside_court_reservation_list
(
    id                  INTEGER PRIMARY KEY AUTO_INCREMENT,

    full_name           VARCHAR(255),
    purpose             VARCHAR(255),
    number_of_attendees INTEGER,

    reservation_date    VARCHAR(255),
    reservation_time    VARCHAR(255),

    resident_id         VARCHAR(255),

    FOREIGN KEY (resident_id) REFERENCES resident (id)
);

CREATE TABLE tennis_court_reservation_List
(
    id                  INTEGER PRIMARY KEY AUTO_INCREMENT,

    full_name           VARCHAR(255),
    purpose             VARCHAR(255),
    number_of_attendees INTEGER,

    reservation_date    VARCHAR(255),
    reservation_time    VARCHAR(255),

    resident_id         VARCHAR(255),

    FOREIGN KEY (resident_id) REFERENCES resident (id)
);

CREATE TABLE items
(
    id            INTEGER PRIMARY KEY AUTO_INCREMENT,
    item_name     VARCHAR(255),
    item_quantity INTEGER
);


CREATE TABLE item_rentals
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
# INSERT INTO barangay_official(id, role, photo, full_name, sex, username, password, birthdate, relocation_year,
#                               address)

# VALUES (UUID(),
#         'barangay_official',
#         null,
#         'Dylan Louis Tayag',
#         'Male',
#         'ghandylan',
#         'password',
#         '1999-09-09',
#         '2000',
#         'Brgy. Maligaya, San Jose City, Nueva Ecija');

