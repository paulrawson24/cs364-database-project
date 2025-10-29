# @Author Trent Davis
# Date: 10/28/2025

import mysql.connector
from mysql.connector import Error as e

class Database:

    """ Block comment
    
    load sql driver: mysql.connector

    set up our database(script)

    connect to the database

    insert/modify/delete data

    query data
    
    disconnect from the database

    """

    # NOTE: Nothing has been tested yet as we have not connected to the database yet

    # this initalizes the connection to the database (our constructor)
    def __init__ (self):
        self.url = "138.49.184.123"
        self.port = "3306"
        self.dbName = "davis3274_a4" # change as needed in accordance with our actual database name
        self.username = "davis3274" # change as needed
        self.password = "" # blank for now until we start testing
        self.connection = None # we're not connecting yet
        # might have to add a cursor object for running queries?

    # This will construct the URL and connect to the database
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.url,
                port = self.port,
                database = self.dbName,
                user = self.username,
                password = self.password
            )
            if self.connection.is_connected():
                print("Successfully connected to MySQL database.")
                return self.connection
        except e:
            print(f"Error connecting to MySQl: {e}")
        return None
    
    # This will close the database connection
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

    # define necessary methods below
    # Database() constructor - done
    # connect() - done 
    # disconnect() - done
    # runquery()
    # other various methods

    # work off template provided in java