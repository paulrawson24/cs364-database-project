# This file is the UI Outline for the player stats table
# @Author Trent Davis
# Date: 11/12/2025

import tkinter as tk
from tkinter import ttk

class StatsTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ## ==== Top Frame - filters ====
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        # Filter by player name
        ttk.Label(self.top_frame, text="Player Name:").pack(side="left", padx=(0,5))
        self.player_filter = ttk.Entry(self.top_frame, width=20)
        self.player_filter.pack(side="left", padx=(0, 15))

        # Filter by game week
        ttk.Label(self.top_frame, text="Week:").pack(side="left", padx=(0,5))
        self.week_filter = ttk.Combobox(
            self.top_frame,
            values=[str(i) for i in range(1, 19)],
            width=5
        )
        self.week_filter.pack(side="left", padx=(0, 15))

        # Buttons
        ttk.Button(self.top_frame, text="Search", command=self.search_stats).pack(side="left", padx=5)
        ttk.Button(self.top_frame, text="Clear", command=self.clear_filters).pack(side="left", padx=5)


        ## ==== Middle Frame - treeview ====
        self.middle_frame = ttk.Frame(self)
        self.middle_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = (
            "stat_id",
            "player_name",
            "game_id",
            "yards",
            "touchdowns",
            "interceptions"
        )

        self.tree = ttk.Treeview(
            self.middle_frame,
            columns=columns,
            show="headings",
            height=12
        )
        self.tree.pack(side="left", fill="both", expand=True)

        # Column headings
        self.tree.heading("stat_id", text="Stat ID")
        self.tree.heading("player_name", text="Player")
        self.tree.heading("game_id", text="Game ID")
        self.tree.heading("yards", text="Yards")
        self.tree.heading("touchdowns", text="TDs")
        self.tree.heading("interceptions", text="INTs")

        # Column widths
        self.tree.column("stat_id", width=80, anchor="center")
        self.tree.column("player_name", width=200, anchor="w")
        self.tree.column("game_id", width=100, anchor="center")
        self.tree.column("yards", width=100, anchor="center")
        self.tree.column("touchdowns", width=80, anchor="center")
        self.tree.column("interceptions", width=80, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.middle_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Insert dummy stats
        self.insert_dummy_data()


        ## ==== Bottom Frame - CRUD buttons ====
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(self.bottom_frame, text="Add Stat", command=self.add_stat).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Edit Stat", command=self.edit_stat).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Delete Stat", command=self.delete_stat).pack(side="left", padx=5)
        ttk.Button(self.bottom_frame, text="Refresh", command=self.refresh_table).pack(side="left", padx=5)


    # This will eventually get changed for real data from mySQL
    ## ===== Dummy Data Function =====
    def insert_dummy_data(self):
        dummy_stats = [
            (1, "Jordan Love", 1, 245, 2, 1),
            (2, "Amon-Ra St. Brown", 3, 115, 1, 0),
            (3, "Justin Jefferson", 2, 140, 1, 0),
            (4, "Josh Allen", 3, 310, 3, 2),
        ]
        for row in dummy_stats:
            self.tree.insert("", "end", values=row)

    # These do not do anything at the moment
    ## ===== Placeholder Methods =====
    def search_stats(self):
        print("Search Stats clicked")

    def clear_filters(self):
        self.player_filter.delete(0, tk.END)
        self.week_filter.set("")
        print("Filters cleared")

    def add_stat(self):
        print("Add Stat clicked")

    def edit_stat(self):
        print("Edit Stat clicked")

    def delete_stat(self):
        print("Delete Stat clicked")

    def refresh_table(self):
        print("Refresh table clicked")