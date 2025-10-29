# This file is the UI Outline for the player_stats table
# @Author Trent Davis
# Date: 10/29/2025
import tkinter as tk
from tkinter import ttk

class StatsTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # ==== Top Frame - filters and search ====
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        # Continue below later