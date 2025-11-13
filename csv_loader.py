# @Author Trent Davis
# CSV loading utilities for the NFL Analytics Dashboard
# Date: 11/12/2025
#
# This module provides helper functions to load CSV files from the
# /csv_files directory and return their rows as Python dictionaries.
#
# Purpose:
#   - Separate CSV parsing logic from database logic
#   - Make it easy for Paul (or anyone) to import CSV rows into MySQL
#   - Allow UI or database code to access clean, ready-to-insert data
#
# How to use:
#   from csv_loader import load_players_csv
#   rows = load_players_csv()
#   for row in rows:
#       print(row)
#
# After loading:
#   Paul will write insert functions in Database.py and loop through
#   each row returned by these loaders.

import csv
import os

# All CSV files are stored in:
#   /csv_files
CSV_FOLDER = "csv_files"


def load_csv(filename):
    """
    Generic CSV loader.
    Given a filename, this function:
      - Builds the correct path to the CSV file inside /csv_files
      - Opens the file
      - Uses csv.DictReader to read each row as a dictionary
      - Returns a list of dictionaries (one per row)

    Parameters:
      filename (str): Name of the CSV file inside /csv_files

    Returns:
      List[Dict[str, str]]: A list of rows where each row is a dictionary
    """

    # Build path like: csv_files/players_2024.csv
    path = os.path.join(CSV_FOLDER, filename)

    rows = []
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    return rows


# ---- Specific table loaders (for convenience) ----
# These wrapper functions make the code cleaner in Database.py.
# Each one simply calls load_csv() with the appropriate filename.

def load_players_csv():
    """Load players_2024.csv and return list of row dictionaries."""
    return load_csv("players_2024.csv")

def load_teams_csv():
    """Load teams_2024.csv and return list of row dictionaries."""
    return load_csv("teams_2024.csv")

def load_games_csv():
    """Load games_2024.csv and return list of row dictionaries."""
    return load_csv("games_2024.csv")

def load_player_stats_csv():
    """Load player_stats_2024.csv and return list of row dictionaries."""
    return load_csv("player_stats_2024.csv")

def load_season_summary_csv():
    """Load season_summary_2024.csv and return list of row dictionaries."""
    return load_csv("season_summary_2024.csv")