# NFL Analytics Dashboard

## Overview
The **NFL Analytics Dashboard** is a Python-based desktop application designed to store, analyze, and visualize player and team statistics from the **2024 NFL season**. Built with **MySQL** and a **Tkinter** GUI, this project allows users to explore key metrics such as passing yards, win/loss records, scoring averages, and player efficiency through advanced queries and visual summaries.

This project was created for our **CS 364 Database Application Project** at the University of Wisconsin–La Crosse.

---

## Team Members
- **Trent Davis**
- **Paul Rawson**

## Features
- **CRUD Operations:** Add, view, update, and delete player, team, and game data  
- **Advanced Queries (Examples):**  
  - Average passing yards per team  
  - Top 10 players by total touchdowns  
  - Win–loss differentials by conference/division  
  - Home vs away performance comparisons  

- **User-Friendly GUI:** Built using Tkinter for a simple desktop experience

---

## Database Design
The relational database models a single NFL season using the following entities:  
- **Teams** – team ID, name, conference, division  
- **Players** – player ID, name, position, team ID  
- **Games** – game ID, week, date, home/away teams, scores  
- **PlayerStats** – stat ID, player ID, game ID, yards, touchdowns, interceptions, etc.  
- *(Optional)* **SeasonSummary** – aggregated team performance  

---

## Technical Requirements
- **Programming Language:** Python 
- **GUI Framework:** Tkinter  
- **Database Platform:** MySQL (via `mysql-connector-python`)  
- **IDE / Editor:** Visual Studio Code  
- **Version Control:** GitHub (shared repository)  
- **Diagram Tool:** Canva (for ER diagram creation)  
- **Data Source:** 2024 NFL season statistics (from ESPN)