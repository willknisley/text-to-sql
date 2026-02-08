import sqlite3
#from openai import OpenAI
#client = OpenAI()

sqliteConnection = sqlite3.connect("rental.db")
cursor = sqliteConnection.cursor()
print("Connected to db")

create_table_vehicles = """CREATE TABLE vehicles (
  vehicle_id INTEGER,
  make VARCHAR(50),
  model VARCHAR(50),
  year INTEGER,
  vehicle_type VARCHAR(50),
  mileage INTEGER,
  status INTEGER,
  PRIMARY KEY (vehicle_id)
)"""
cursor.execute(create_table_vehicles
)

create_table_customers = """CREATE TABLE customers (
  customer_id INTEGER,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  phone INTEGER,
  license_number VARCHAR(10),
  PRIMARY KEY (customer_id)
)"""
cursor.execute(create_table_customers)

create_table_locations = """ CREATE TABLE locations (
  location_id INTEGER,
  name VARCHAR(50),
  city VARCHAR(50),
  capacity INTEGER,
  PRIMARY KEY (location_id)
)"""
cursor.execute(create_table_locations
)

create_table_rentals = """ CREATE TABLE rentals (
  rental_id INTEGER,
  vehicle_id INTEGER,
  customer_id INTEGER,
  pickup_location_id INTEGER,
  return_location_id INTEGER,
  start_date TIMESTAMP,
  end_date TIMESTAMP,
  actual_return_date TIMESTAMP,
  total_cost INTEGER,
  PRIMARY KEY (rental_id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles (vehicle_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (pickup_location_id) REFERENCES locations (location_id),
  FOREIGN KEY (return_location_id) REFERENCES locations (location_id)
)"""
cursor.execute(create_table_rentals)


insert_customers = """INSERT INTO customers (customer_id, first_name, last_name, phone, license_number)
VALUES
(1, 'John', 'Smith', 5551234, 'D1234567'),
(2, 'Emily', 'Johnson', 5552345, 'D2345678'),
(3, 'Michael', 'Brown', 5553456, 'D3456789'),
(4, 'Sarah', 'Davis', 5554567, 'D4567890'),
(5, 'David', 'Wilson', 5555678, 'D5678901'),
(6, 'Jessica', 'Taylor', 5556789, 'D6789012'),
(7, 'Daniel', 'Moore', 5557890, 'D7890123'),
(8, 'Ashley', 'Martin', 5558901, 'D8901234'),
(9, 'Chris', 'Lee', 5559012, 'D9012345'),
(10, 'Amanda', 'Clark', 5550123, 'D0123456');"""

insert_vehicles = """ INSERT INTO vehicles (vehicle_id, make, model, year, vehicle_type, mileage, status)
VALUES
(1, 'Toyota', 'Camry', 2021, 'Sedan', 32000, 'available'),
(2, 'Honda', 'Civic', 2020, 'Sedan', 41000, 'rented'),
(3, 'Ford', 'Explorer', 2022, 'SUV', 18000, 'available'),
(4, 'Chevrolet', 'Malibu', 2019, 'Sedan', 52000, 'maintenance'),
(5, 'Nissan', 'Rogue', 2021, 'SUV', 29000, 'available'),
(6, 'Jeep', 'Wrangler', 2023, 'SUV', 9000, 'rented'),
(7, 'Hyundai', 'Elantra', 2020, 'Sedan', 47000, 'available'),
(8, 'Kia', 'Sorento', 2022, 'SUV', 21000, 'available'),
(9, 'Tesla', 'Model 3', 2023, 'Electric', 8000, 'rented'),
(10, 'Subaru', 'Outback', 2021, 'Wagon', 35000, 'available');"""

insert_locations = """ INSERT INTO locations (location_id, name, city, capacity)
VALUES
(1, 'Downtown Branch', 'Salt Lake City', 50),
(2, 'Airport Branch', 'Salt Lake City', 100),
(3, 'West Side', 'Ogden', 40),
(4, 'East Side', 'Provo', 45),
(5, 'Central Hub', 'Logan', 35),
(6, 'North Station', 'Layton', 30),
(7, 'South Station', 'Orem', 30),
(8, 'City Center', 'Park City', 25),
(9, 'Highland Office', 'Lehi', 20),
(10, 'University Branch', 'Provo', 15);"""

insert_rentals = """ INSERT INTO rentals (rental_id, vehicle_id, customer_id, pickup_location_id, return_location_id, start_date, end_date, actual_return_date, total_cost)
VALUES
(1, 2, 1, 1, 2, '2026-01-01 09:00:00', '2026-01-05 09:00:00', '2026-01-05 08:45:00', 320),
(2, 6, 2, 2, 2, '2026-01-03 10:00:00', '2026-01-06 10:00:00', NULL, 210),
(3, 9, 3, 1, 3, '2026-01-07 08:30:00', '2026-01-10 08:30:00', NULL, 450),
(4, 1, 4, 4, 4, '2026-01-02 12:00:00', '2026-01-04 12:00:00', '2026-01-04 11:50:00', 150),
(5, 5, 5, 5, 6, '2026-01-08 09:15:00', '2026-01-11 09:15:00', NULL, 275),
(6, 3, 6, 3, 1, '2026-01-09 14:00:00', '2026-01-12 14:00:00', NULL, 360),
(7, 7, 7, 6, 6, '2026-01-01 16:00:00', '2026-01-03 16:00:00', '2026-01-03 15:55:00', 140),
(8, 8, 8, 8, 9, '2026-01-10 11:00:00', '2026-01-13 11:00:00', NULL, 310),
(9, 10, 9, 9, 9, '2026-01-05 13:00:00', '2026-01-07 13:00:00', '2026-01-07 12:40:00', 180),
(10, 4, 10, 10, 1, '2026-01-06 15:30:00', '2026-01-09 15:30:00', '2026-01-09 15:20:00', 260);"""