import mysql.connector

class Database:
    
    try:
    # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
            # update these with necessary information
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
    # might need a finally clause below this except?

    # define necessary methods below
    # Database() constructor
    # connect()
    # disconnect()
    # runquery()

    # work off template provided in java

    # This class will be used to connect / disconnect 
    # and do other various operations with the database
