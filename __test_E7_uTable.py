import sqlite3
import pytest

def get_users_table_columns(cursor):
    cursor.execute("PRAGMA table_info(Users)")
    columns = cursor.fetchall()
    return [column[1] for column in columns]

def test_users_table_columns_exist():
    # Connect to your database (replace 'your_database.db' with your database file)
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Get the columns of the 'Users' table
    table_columns = get_users_table_columns(cursor)

    # Define the expected column names
    expected_columns = [
        'username', 'password', 'firstName', 'lastName', 'marketingEmail', 'marketingSMS',
        'adsTargeted', 'language', 'userMajor', 'userUniversity'
    ]

    # Check if the expected columns exist in the schema
    for column_name in expected_columns:
        assert column_name in table_columns

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    pytest.main([__file__])
