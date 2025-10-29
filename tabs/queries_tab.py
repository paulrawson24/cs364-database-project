# This file is the UI outline for our advanced queries
# @Author Trent Davis
# Date: 10/29/2025
import tkinter as tk
from tkinter import ttk

class QueriesTab(ttk.Frame):
    def __init__(self, parent):
        super().__init_(parent)

        # ==== Top Frame (buttons) ====
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        # Continue below later