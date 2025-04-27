import mysql.connector

# Function to collect employee information from the user
def collect_employee_data(employee_data):
    while True:
        print("\nEnter employee information (or 'q' to quit):")
        
        employee_name = input("Enter employee name: ")
        if employee_name.lower() == 'q':
            break
        
        employee_address = input("Enter employee address: ")
        employee_designation = input("Enter employee designation: ")

        # Input validation
        if not employee_name or not employee_address or not employee_designation:
            print("Error: All fields must be filled. Please try again.")
            continue

        # Additional validation logic (e.g., checking if the name is unique) can be added here

        employee_data.append((employee_name, employee_address, employee_designation))

    return employee_data

# Function to display employee data
def display_employee_data(employee_data):
    print("\nEmployee data collected:")
    for employee in employee_data:
        print(employee)

# Function to save data to the MySQL database
def save_to_mysql(employee_data):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="devlimbachiya",
            database="dev"
        )
        cursor = connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            employee_name VARCHAR(255) NOT NULL,
            employee_address VARCHAR(255) NOT NULL,
            employee_designation VARCHAR(255) NOT NULL
        );
        """
        cursor.execute(create_table_query)

        insert_query = "INSERT INTO employees (employee_name, employee_address, employee_designation) VALUES (%s, %s, %s)"
        cursor.executemany(insert_query, employee_data)

        connection.commit()
        print("Data has been saved to the MySQL database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    employee_data = []
    
    while True:
        print("\n1. Enter new employee data")
        print("2. View collected employee data")
        print("3. Save data to MySQL database")
        print("4. Quit")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        
        if choice == "1":
            employee_data = collect_employee_data(employee_data)
        elif choice == "2":
            display_employee_data(employee_data)
        elif choice == "3":
            save_to_mysql(employee_data)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
