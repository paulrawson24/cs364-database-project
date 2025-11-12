# This file is where we will run the main method for our NFL Analytics Dashboard
# The 'UI Manager'
# @Author Trent Davis & Paul Rawson
# Date: 11/12/2025
import tkinter as tk
from tkinter import ttk

# Import tab classes below
from tabs.games_tab import GamesTab
from tabs.players_tab import PlayersTab
from tabs.queries_tab import QueriesTab
from tabs.stats_tab import StatsTab
from tabs.teams_tab import TeamsTab

class NFLDashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()

        ## ==== Window Configuration ====
        self.title("NFL Analytics Dashboard")
        self.geometry("1000x700")
        self.resizable(True, True)

        # Styling we can do in ttk
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TNotebook.tab", padding=[15,5])
        style.configure("TButton", font=("Helvetica", 10))
        style.configure("TLabel", font=("Helvetica", 10))

        # ==== Title Label ====
        title_label = ttk.Label(
            self,
            text="NFL Analytics Dashboard (2024 Season)",
            font=("Helvetica", 18, "bold")
        )
        title_label.pack(pady=15)

        # ==== Notebook Setup ====
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # ==== Create Tab Instances ====
        self.players_tab = PlayersTab(notebook)
        self.teams_tab = TeamsTab(notebook)
        self.games_tab = GamesTab(notebook)
        self.stats_tab = StatsTab(notebook)
        self.queries_tab = QueriesTab(notebook)

        # ==== Add Tabs to Notebook ====
        notebook.add(self.players_tab, text="Players")
        notebook.add(self.teams_tab, text="Teams")
        notebook.add(self.games_tab, text="Games")
        notebook.add(self.stats_tab, text="Player Stats")
        notebook.add(self.queries_tab, text="Advanced Queries")

def main():
    app = NFLDashboardApp()
    app.mainloop()


if __name__ == "__main__":
    main()