# This file is the UI Outline for the teams table
# @Author Trent Davis
# Date: 11/12/2025

import tkinter as tk
from tkinter import ttk

class TeamsTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ## ==== Top Frame - filters and search ====
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        # Filter by Conference
        ttk.Label(self.top_frame, text="Conference:").pack(side="left", padx=(0,5))
        self.conference_filter = ttk.Combobox(
            self.top_frame,
            values=["AFC", "NFC"],
            width=10
        )
        self.conference_filter.pack(side="left", padx=(0, 15))

        # Filter by Division
        ttk.Label(self.top_frame, text="Division:").pack(side="left", padx=(0,5))
        self.division_filter = ttk.Combobox(
            self.top_frame,
            values=["North", "South", "East", "West"],
            width=10
        )
        self.division_filter.pack(side="left", padx=(0, 15))

        # Buttons
        ttk.Button(self.top_frame, text="Search", command=self.search_teams).pack(side="left", padx=5)
        ttk.Button(self.top_frame, text="Clear", command=self.clear_filters).pack(side="left", padx=5)


        ## ==== Middle Frame - treeview (table) ====
        self.middle_frame = ttk.Frame(self)
        self.middle_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("team_id", "name", "conference", "division")

        self.tree = ttk.Treeview(
            self.middle_frame,
            columns=columns,
            show="headings",
            height=12
        )
        self.tree.pack(side="left", fill="both", expand=True)

        # Column headers
        self.tree.heading("team_id", text="ID")
        self.tree.heading("name", text="Team Name")
        self.tree.heading("conference", text="Conference")
        self.tree.heading("division", text="Division")

        # Column widths
        self.tree.column("team_id", width=60, anchor="center")
        self.tree.column("name", width=200, anchor="w")
        self.tree.column("conference", width=120, anchor="center")
        self.tree.column("division", width=120, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.middle_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Insert dummy teams
        self.insert_dummy_data()


        ## ==== Bottom Frame - CRUD buttons ====
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(self.bottom_frame, text="Add Team", command=self.add_team).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Edit Team", command=self.edit_team).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Delete Team", command=self.delete_team).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Refresh", command=self.refresh_table).pack(side="left", padx=5)


    # This will eventually get changed for real data from mySQL
    ## ===== Dummy Data Function =====
    def insert_dummy_data(self):
        dummy_teams = [
            (1, "Green Bay Packers", "NFC", "North"),
            (2, "Chicago Bears", "NFC", "North"),
            (3, "Minnesota Vikings", "NFC", "North"),
            (4, "Detroit Lions", "NFC", "North"),
            (5, "Kansas City Chiefs", "AFC", "West"),
            (6, "Buffalo Bills", "AFC", "East"),
        ]
        for row in dummy_teams:
            self.tree.insert("", "end", values=row)

    # These do not do anything at the moment
    ## ===== Placeholder Functions =====
    def search_teams(self):
        print("Search Teams clicked")

    def clear_filters(self):
        self.conference_filter.set("")
        self.division_filter.set("")
        print("Filters cleared")

    def add_team(self):
        print("Add Team clicked")

    def edit_team(self):
        print("Edit Team clicked")

    def delete_team(self):
        print("Delete Team clicked")

    def refresh_table(self):
        print("Refresh table clicked")