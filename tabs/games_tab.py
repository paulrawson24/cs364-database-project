# This file is the UI Outline for the games table
# @Author Trent Davis
# Date: 11/12/2025

import tkinter as tk
from tkinter import ttk

class GamesTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ## ==== Top Frame - filters and search ====
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        # Filter by week
        ttk.Label(self.top_frame, text="Week:").pack(side="left", padx=(0,5))
        self.week_filter = ttk.Combobox(
            self.top_frame,
            values=[str(i) for i in range(1, 19)],  # NFL 18 weeks
            width=5
        )
        self.week_filter.pack(side="left", padx=(0, 15))

        # Filter by team
        ttk.Label(self.top_frame, text="Team:").pack(side="left", padx=(0,5))
        self.team_filter = ttk.Entry(self.top_frame, width=20)
        self.team_filter.pack(side="left", padx=(0, 15))

        # Buttons
        ttk.Button(self.top_frame, text="Search", command=self.search_games).pack(side="left", padx=5)
        ttk.Button(self.top_frame, text="Clear", command=self.clear_filters).pack(side="left", padx=5)


        ## ==== Middle Frame - treeview ====
        self.middle_frame = ttk.Frame(self)
        self.middle_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = (
            "game_id",
            "week",
            "date",
            "home_team",
            "away_team",
            "home_score",
            "away_score"
        )

        self.tree = ttk.Treeview(
            self.middle_frame,
            columns=columns,
            show="headings",
            height=12
        )
        self.tree.pack(side="left", fill="both", expand=True)

        # Column headings
        self.tree.heading("game_id", text="ID")
        self.tree.heading("week", text="Week")
        self.tree.heading("date", text="Date")
        self.tree.heading("home_team", text="Home Team")
        self.tree.heading("away_team", text="Away Team")
        self.tree.heading("home_score", text="Home Score")
        self.tree.heading("away_score", text="Away Score")

        # Column widths / alignment
        self.tree.column("game_id", width=60, anchor="center")
        self.tree.column("week", width=70, anchor="center")
        self.tree.column("date", width=120, anchor="center")
        self.tree.column("home_team", width=150, anchor="w")
        self.tree.column("away_team", width=150, anchor="w")
        self.tree.column("home_score", width=100, anchor="center")
        self.tree.column("away_score", width=100, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.middle_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Dummy data for testing
        self.insert_dummy_data()


        ## ==== Bottom Frame - CRUD buttons ====
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(self.bottom_frame, text="Add Game", command=self.add_game).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Edit Game", command=self.edit_game).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Delete Game", command=self.delete_game).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Refresh", command=self.refresh_table).pack(side="left", padx=5)


    # This will eventually get changed for real data from mySQL
    ## ===== Dummy Data Function =====
    def insert_dummy_data(self):
        dummy_games = [
            (1, 1, "2024-09-07", "Packers", "Bears", 24, 17),
            (2, 2, "2024-09-14", "Vikings", "Lions", 31, 27),
            (3, 3, "2024-09-21", "Chiefs", "Bills", 35, 28),
            (4, 4, "2024-09-28", "49ers", "Rams", 30, 20),
        ]
        for row in dummy_games:
            self.tree.insert("", "end", values=row)

    # These do not do anything at the moment
    ## ===== Placeholder Methods for CRUD =====
    def search_games(self):
        print("Search games clicked")

    def clear_filters(self):
        self.week_filter.set("")
        self.team_filter.delete(0, tk.END)
        print("Filters cleared")

    def add_game(self):
        print("Add Game clicked")

    def edit_game(self):
        print("Edit Game clicked")

    def delete_game(self):
        print("Delete Game clicked")

    def refresh_table(self):
        print("Refresh table clicked")