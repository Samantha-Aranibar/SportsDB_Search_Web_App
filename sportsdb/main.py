from sportsdb.project import SportsDBClient

def print_team(team: dict):
    print("\n--- Team Info ---")
    print("Team Name:    ", team.get("strTeam", "N/A"))
    print("Country:    ", team.get("strCountry","N/A"))
    print("League:    ",team.get("strLeague","N/A"))
    print("Stadium:    ",team.get("strStadium","N/A"))

def print_player(player: dict):
    print("\n--- Player Info ---")
    print("Player Name:    ", player.get("strPlayer", "N/A"))
    print("Team:    ", player.get("strTeam", "N/A"))
    print("Position:    ", player.get("strPosition", "N/A"))

def main():
    client = SportsDBClient()

    team_name = input("Enter a soccer team name:  ").strip()
    if not team_name:
        print("No team name entered!")
        return
    data = client.search_team(team_name)
    teams = data.get("teams")
    if not teams:
        print("No teams found.")
        return    
    print_team(teams[0])


    player_name = input("Enter a player name: ").strip()
    if not player_name:
        print("No player name entered!")
        return
    player_data = client.search_player(player_name)
    players = player_data.get("player")  
    if not players:
        print("No players found. ")
        return
    print_player(players[0])



if __name__ == "__main__":
    main()

