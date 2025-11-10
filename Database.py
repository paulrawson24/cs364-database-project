# @Author Trent Davis & Paul Rawson
# Date: 10/28/2025

import mysql.connector
from mysql.connector import Error

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
        self.dbName = "rawson7711_nflDbProject"
<<<<<<< HEAD
        self.username = "rawson7711" # Using Pauls username and password
        self.password = "!kcj9qQ6LNVD3nEzm"
=======
        self.username = "davis3274" # change as needed
        self.password = "" # blank for now until we start testing
>>>>>>> origin/main
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

    # some various methods that we may need also:
    # def get_players():
    # def insert_player(data):
    # def update_player(player_id, data):
    # def delete_player(player_id):

    # work off template provided in java

    # -------------------------
    # teams operations
    # -------------------------

    # Insert: add a new team record to teams table
    # Read: retrieve all teams
    # Update: Modify an existing teams details like name/division
    # Delele: Remove a team record from db

    # -------------------------
    # Players table operations
    # -------------------------

    # Insert: add a new player w attributes like name, position, etc.
    # Read: get all players or players by team
    # update: edit player info
    # Delete: Remove a player from the db

    # -------------------------
    # Games table operations
    # -------------------------

    # Insert: create a new game entry with week, date, and teams
    # Read: retrieve all games or filter by week/date
    # Update: update game scores, etc.
    # Delete: delete a specific game entry

    # -------------------------
    # Player Stats table operations
    # -------------------------

    # Insert: add player stats for given game
    # Read: retrieve all player stats or for specfic player/game
    # Update: Modify stat values (yards, tds, etc.)
    # Delete: Remove a players stat record

    # -------------------------
    # Season summary table operations
    # -------------------------

    # Read: generate aggregated season summaries per team

    # -------------------------
    # Advanced Queries
    # -------------------------

    # calculate average passing/rushing/recieving yards per game for a player
    # get top players by a certain stat like TDs
    # calculate win-loss differentials by division
    # compare home vs away performance metrics
    # Identify teams w/ highest offensive efficiency

 

# to test db connection
if __name__ == "__main__":
    print("Attempting to connect to database...")
    db = Database()
    conn = db.connect()

    if conn:
        print("Connection test successful!")
        try:
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES;")
            print("\nDatabases visible to this user:")
            for (name,) in cursor.fetchall():
                print(f" - {name}")
            cursor.close()
        except Exception as err:
            print(f"Error running test query: {err}")
        db.disconnect()
    else:
        print("Connection test failed.")