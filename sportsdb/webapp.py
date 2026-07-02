from flask import Flask, jsonify, request, render_template
from sportsdb.project import SportsDBClient

app = Flask(__name__)
client = SportsDBClient()

@app.route('/') #('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/search") #('/search', methods=['GET'])
def search():
    query = request.args.get("q","").strip()
    mode = request.args.get("mode","player") # 'player' or 'team'

    if not query:
        return render_template("results.html", error="Please enter a name.")
    
    try:
        if mode == "team":
            data = client.search_team(query)
            items = data.get("teams") # teams endpoint uses "teams"
            if not items:
                return render_template("results.html", error="No teams found.")
            teams = items[0]
            return render_template("results.html", 
                                   mode = "team",
                                   name = teams.get("strTeam"),
                                   subtitle = teams.get("strLeague"),
                                   image_url = teams.get("strBadge"),
                                   extra = {
                                       "Sport" : teams.get("strSport"),
                                       "Country": teams.get("strCountry"),
                                       "Stadium": teams.get("strStadium"),
                                       "Description": teams.get("strDescriptionEN"),
                                       "Banner": teams.get("strBanner"),
                                       "Fanart1": teams.get("strFanart1")
                                   },)
        #PLAYER_MODE
        data = client.search_player(query)
        p_items = data.get("player")
        if not p_items:
            return render_template("results.html", error= "No players found.")
        players = p_items[0]
        return render_template("results.html", 
                               mode = "player",
                               name = players.get("strPlayer"),
                               subtitle = players.get("strTeam"),
                               image_url = players.get("strThumb"),
                               extra = {
                                   "Sport" : players.get("strSport"),
                                   "Nationality" : players.get("strNationality"),
                                   "Position" : players.get("strPosition"),
                                   "Born" : players.get("dateBorn"),
                                   "Gender" : players.get("strGender"),
                                   "Cutout" : players.get("strCutout"),
                               },)
    except Exception as e:
        return render_template("results.html", error=f"Error: {e}")
    
if __name__ == "__main__":
    app.run(debug=True)


