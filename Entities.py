# Entities.py
# @Authors: Paul Rawson
# Purpose: Entity classes representing the tables and relationships from ER Diagram

# PLayer Entity
class Player:
    def __init__(self, player_id=None, first_name=None, last_name=None, position=None, team_id=None):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team_id = team_id

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position} {self.team_id}"


# Team Entity
class Team:
    def __init__(self, team_id=None, team_name=None, conference=None, division=None):
        self.team_id = team_id
        self.team_name = team_name
        self.conference = conference
        self.division = division

    def __str__(self):
        return f"{self.team_name} ({self.conference} {self.division})"
    
# Class Entity
class Game:
    def __init__(self, game_id=None, week=None, date=None, home_team_id=None, away_team_id=None, home_score=None, away_score=None):
        self.game_id = game_id
        self.week = week
        self.date = date
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.home_score = home_score
        self.away_score = away_score

    def __str__(self):
        return f"(Week {self.week}) {self.home_team_id} : {self.home_score} vs. {self.away_team_id} : {self.away_score}"

# PlayerStats Entity
class PlayerStat:
    def __init__(self, player_id=None, player_name=None, player_display_name=None, week=None, team=None, opponent_team=None, completions=None, attempts=None,
                 passing_yards=None, passing_tds=None, passing_interceptions=None, rushing_yards=None, rushing_tds=None, receptions=None,
                 recieving_yards=None, recieving_tds=None, def_sacks=None, def_interceptions=None, game_id=None, stat_id=None):
        self.player_id = player_id
        self.player_name = player_name
        self.player_display_name = player_display_name
        self.week = week
        self.team = team
        self.opponent_team = opponent_team
        self.completions = completions
        self.attempts = attempts
        self.passing_yards = passing_yards
        self.passing_tds = passing_tds
        self.passing_interceptions = passing_interceptions
        self.rushing_yards = rushing_yards
        self.rushing_tds = rushing_tds
        self.receptions = receptions
        self.recieving_yards = recieving_yards
        self.recieving_tds = recieving_tds
        self.def_sacks = def_sacks
        self.def_interceptions = def_interceptions
        self.game_id = game_id
        self.stat_id = stat_id

    def __str__(self):
        return f"{}"

# SeasonSummary Entity
class SeasonSummary:
   # continue later