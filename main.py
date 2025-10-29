# This file is where we will run the main method for our NFL Analytics Dashboard
# The 'UI Manager'
# @Author Trent Davis & Paul Rawson
# Date: 10/29/2025
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

        # Continue below later



# leave this for later
def main():
    pass





if __name__ == "__main__":
    main()