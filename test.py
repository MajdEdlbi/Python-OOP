import mysql.connector

# 🛠️ Configuration
config = {
  'host': 'localhost',
  'user': 'root',
  'passwd': '',
  'database': 'school' # Ensure this database exists on your server
}

# --- Database Connection and Setup ---
try:
    mydb = mysql.connector.connect(**config)
    if mydb.is_connected():
        print("✅ Connected to MySQL database 'school'.")
        mycursor = mydb.cursor()

        # ⚠️ Optional: Create the table if it doesn't exist
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS registration (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                mobile VARCHAR(20),
                course VARCHAR(255)
            )
        """)
        mydb.commit()
        print("✅ Table 'registration' ensured.")

except mysql.connector.Error as err:
    print(f"❌ Error connecting to MySQL: {err}")
    # Exit if connection fails
    exit()

# ------------------------------
## ➕ CREATE (Insert)
# ------------------------------
def create_record(name, mobile, course):
    """Inserts a new registration record."""
    try:
        sql = "INSERT INTO registration (name, mobile, course) VALUES (%s, %s, %s)"
        val = (name, mobile, course)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"\n➕ CREATE: Successfully added **{name}** (Course: {course}, ID: {mycursor.lastrowid}).")
    except Exception as e:
        print(f"❌ Error during CREATE: {e}")

# ------------------------------
## 📖 READ (Select)
# ------------------------------
def read_all_records():
    """Fetches and displays all records from the table."""
    try:
        sql = "SELECT id, name, mobile, course FROM registration"
        mycursor.execute(sql)
        results = mycursor.fetchall()

        print("\n📖 READ: All Registered Records")
        print("-" * 50)
        if not results:
            print("No records found.")
        else:
            for id, name, mobile, course in results:
                print(f"ID: {id}, Name: {name}, Mobile: {mobile}, Course: {course}")
        print("-" * 50)
        return results
    except Exception as e:
        print(f"❌ Error during READ: {e}")
        return []

# ------------------------------
## ✏️ UPDATE
# ------------------------------
def update_course(record_id, new_course):
    """Updates the course for a record given its ID."""
    try:
        sql = "UPDATE registration SET course = %s WHERE id = %s"
        val = (new_course, record_id)
        mycursor.execute(sql, val)
        mydb.commit()
        if mycursor.rowcount > 0:
            print(f"\n✏️ UPDATE: Successfully updated record ID **{record_id}** to course **{new_course}**.")
        else:
            print(f"\n⚠️ UPDATE: Record with ID {record_id} not found.")
    except Exception as e:
        print(f"❌ Error during UPDATE: {e}")

# ------------------------------
## 🗑️ DELETE
# ------------------------------
def delete_record(record_id):
    """Deletes a record given its ID."""
    try:
        sql = "DELETE FROM registration WHERE id = %s"
        val = (record_id,) # The comma is important for a single-item tuple
        mycursor.execute(sql, val)
        mydb.commit()
        if mycursor.rowcount > 0:
            print(f"\n🗑️ DELETE: Successfully deleted record ID **{record_id}**.")
        else:
            print(f"\n⚠️ DELETE: Record with ID {record_id} not found.")
    except Exception as e:
        print(f"❌ Error during DELETE: {e}")


# --- DEMONSTRATION ---
# 1. CREATE three records
create_record("John Doe", "555-1234", "Physics")
create_record("Jane Smith", "555-5678", "Chemistry")
create_record("Mark Twain", "555-9012", "English")

# 2. READ all records
records = read_all_records()

# 3. UPDATE one record (assuming John Doe is ID 1)
update_course(1, "Advanced Physics")

# 4. READ again to see the update
read_all_records()

# 5. DELETE one record (Mark Twain, likely ID 3)
delete_record(3)

# 6. Final READ
read_all_records()

# --- Cleanup ---
mycursor.close()
mydb.close()
print("\n🔌 Connection closed.")
