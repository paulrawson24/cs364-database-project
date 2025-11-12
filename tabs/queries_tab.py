# This file is the UI Outline for the advanced queries tab
# @Author Trent Davis
# Date: 11/12/2025

import tkinter as tk
from tkinter import ttk

class QueriesTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ## ==== Top Frame - Query Buttons ====
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(self.top_frame, text="Select an Analysis:", font=("Helvetica", 12)).pack(
            side="left", padx=(0, 15)
        )

        ttk.Button(self.top_frame, text="Leaderboards", command=self.show_leaderboards).pack(side="left", padx=5)
        ttk.Button(self.top_frame, text="Team Trends", command=self.show_team_trends).pack(side="left", padx=5)
        ttk.Button(self.top_frame, text="Home vs Away", command=self.show_home_away).pack(side="left", padx=5)
        ttk.Button(self.top_frame, text="Rankings", command=self.show_rankings).pack(side="left", padx=5)
        ttk.Button(self.top_frame, text="Consistency", command=self.show_consistency).pack(side="left", padx=5)


        ## ==== Middle Frame - Treeview for Query Results ====
        self.middle_frame = ttk.Frame(self)
        self.middle_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            self.middle_frame,
            columns=("col1", "col2", "col3"),
            show="headings",
            height=12
        )
        self.tree.pack(side="left", fill="both", expand=True)

        # Example column setup (will change dynamically later)
        self.tree.heading("col1", text="Column 1")
        self.tree.heading("col2", text="Column 2")
        self.tree.heading("col3", text="Column 3")

        self.tree.column("col1", anchor="center", width=200)
        self.tree.column("col2", anchor="center", width=200)
        self.tree.column("col3", anchor="center", width=200)

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.middle_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")


        ## ==== Bottom Frame - Clear Button ====
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(self.bottom_frame, text="Clear Results", command=self.clear_results).pack(side="left", padx=5)

    # These do not do anything at the moment
    # ===== Placeholder Query Methods =====
    def show_leaderboards(self):
        print("Leaderboards query clicked")

    def show_team_trends(self):
        print("Team Trends query clicked")

    def show_home_away(self):
        print("Home vs Away query clicked")

    def show_rankings(self):
        print("Rankings query clicked")

    def show_consistency(self):
        print("Consistency query clicked")


    # ===== Clear the Treeview =====
    def clear_results(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        print("Results cleared")