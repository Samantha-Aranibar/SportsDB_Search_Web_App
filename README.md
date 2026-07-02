# SportsDB Search Web App

A Python and Flask web application that searches for soccer teams and players using TheSportsDB API.

The project includes both a command-line interface and a web interface. Users can search for a team or player and view information such as league, country, stadium, position, nationality, and images when available.

---

## Features

- Search for soccer teams
- Search for soccer players
- Display team and player details
- Display images from API results
- Flask web interface
- Command-line version
- Uses environment variables for API configuration

---

## Technologies Used

- Python
- Flask
- Requests
- python-dotenv
- HTML
- Jinja2 Templates
- TheSportsDB API

---

## Repository Structure

```text
SportsDB-Search-Web-App/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
│
├── sportsdb/
│   ├── __init__.py
│   ├── project.py
│   ├── main.py
│   └── webapp.py
│
└── templates/
    ├── index.html
    └── results.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/SportsDB-Search-Web-App.git
cd SportsDB-Search-Web-App
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```text
SPORTSDB_API_KEY=your_api_key_here
```

An example file is included as:

```text
.env.example
```

---

## Running the Web App

```bash
python sportsdb/webapp.py
```

Then open your browser and go to:

```text
http://localhost:5000
```

---

## Running the Command-Line App

```bash
python sportsdb/main.py
```

---

## Example Searches

Team search:

```text
Arsenal
```

Player search:

```text
Messi
```

---

## Current Limitations

- Search results display the first matching team or player.
- The app currently focuses on teams and players.
- API data depends on TheSportsDB response availability.

---

## Skills Demonstrated

- Python programming
- Flask web development
- REST API integration
- Environment variable management
- HTML templates
- JSON response handling
- Command-line application development
- Web application development

---

## Future Improvements

- Add Bootstrap styling
- Display multiple search results
- Add league search
- Add favorite teams or players
- Add error handling for missing images
- Add tests
- Deploy the application online

---

## Author

Samantha Aranibar
