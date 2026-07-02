import requests
from dotenv import dotenv_values

BASE_URL = "https://www.thesportsdb.com/api/v1/json"
#url = "https://www.thesportsdb.com/api/v1/json/3/all_sports.php"

#response = requests.get(url)
#print(response.json())

class SportsDBClient:
    def __init__(self):
        config = dotenv_values(".env")
        self.api_key = config.get("SPORTSDB_API_KEY")

        if not self.api_key:
            raise ValueError(
                "SPORTSDB_API_KEY not found in .env file"
            )
        
    def search_team(self, team_name: str) -> dict:
        url = f"{BASE_URL}/{self.api_key}/searchteams.php"
        response = requests.get(url, params={"t": team_name}, timeout=20)
        response.raise_for_status()
        return response.json()
    
    def search_player(self,player_name: str) -> dict:
        url = f"{BASE_URL}/{self.api_key}/searchplayers.php"
        response = requests.get(url, params={"p": player_name}, timeout=20)
        response.raise_for_status()
        return response.json()