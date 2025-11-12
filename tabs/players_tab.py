# This file is the UI Outline for the players table
# @Author Trent Davis
# Date: 11/12/2025

import tkinter as tk
from tkinter import ttk

class PlayersTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # NOTE: tab is not fully functional yet, it is just setup for a visual outline

        ## ==== Top Frame - filters and search ====
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        # Filter by team
        ttk.Label(self.top_frame, text="Filter by Team:").pack(side="left", padx=(0,5))
        self.team_filter = ttk.Combobox(self.top_frame, values=["GB", "CHI", "MIN", "DET"], width=10)
        # Just using these as placeholders, we will eventually just get data from mySQL
        self.team_filter.pack(side="left", padx=(0, 15))

        # Search by name
        ttk.Label(self.top_frame, text="Search Name:").pack(side="left", padx=(0,5))
        self.name_search = ttk.Entry(self.top_frame, width=20)
        self.name_search.pack(side="left", padx=(0,10))

        # Buttons
        ttk.Button(self.top_frame, text="Search", command=self.search_players).pack(side="left", padx=5)
        ttk.Button(self.top_frame, text="Clear", command=self.clear_filters).pack(side="left", padx=5)


        ## ==== Middle Frame - treeview (table) ====
        self.middle_frame = ttk.Frame(self)
        self.middle_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("player_id", "name", "position", "team")

        self.tree = ttk.Treeview(
            self.middle_frame,
            columns=columns,
            show="headings",
            height=12
        )
        self.tree.pack(side="left", fill="both", expand=True)

        # Column headers
        self.tree.heading("player_id", text="ID")
        self.tree.heading("name", text="Player Name")
        self.tree.heading("position", text="Position")
        self.tree.heading("team", text="Team")

        # Column widths
        self.tree.column("player_id", width=60, anchor="center")
        self.tree.column("name", width=200, anchor="w")
        self.tree.column("position", width=100, anchor="center")
        self.tree.column("team", width=80, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.middle_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Insert dummy data
        self.insert_dummy_data()


        ## ==== Bottom Frame - CRUD buttons ====
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(self.bottom_frame, text="Add Player", command=self.add_player).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Edit Player", command=self.edit_player).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Delete Player", command=self.delete_player).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Refresh", command=self.refresh_table).pack(side="left", padx=5)

    # This will eventually get changed for real data from mySQL
    # ===== Dummy Data Function =====
    def insert_dummy_data(self):
        dummy_players = [
            (1, "Jordan Love", "QB", "GB"),
            (2, "Aaron Jones", "RB", "MIN"),
            (3, "DJ Moore", "WR", "CHI"),
            (4, "Amon-Ra St. Brown", "WR", "DET"),
        ]
        for row in dummy_players:
            self.tree.insert("", "end", values=row)

    # These do not do anything at the moment
    # ===== Placeholder Functions =====
    def search_players(self):
        print("Search clicked")

    def clear_filters(self):
        print("Clear clicked")
        self.team_filter.set("")
        self.name_search.delete(0, tk.END)

    def add_player(self):
        print("Add Player clicked")

    def edit_player(self):
        print("Edit Player clicked")

    def delete_player(self):
        print("Delete Player clicked")

    def refresh_table(self):
        print("Refresh table clicked")