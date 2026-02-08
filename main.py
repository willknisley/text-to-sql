import sqlite3

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
