# TMDB CLI Tool 🎬

A command-line interface (CLI) application built with Python that interacts with The Movie Database (TMDB) API to fetch and display movie information. This tool allows you to quickly pull the top 5 movies across various categories directly in your terminal. This is a backend practice project on building CLIs (I am very open to your conributions and corrections 😇).

## Features
* **Live Data:** Fetches real-time movie data directly from the TMDB API.
* **Custom Categories:** Filter movies by `playing` (Now Playing), `popular`, `top` (Top Rated), or `upcoming`.
* **Simple CLI:** Easy-to-use argument parsing for quick terminal execution.
* **Robust Error Handling:** Gracefully handles network failures and API errors.

## Prerequisites
Before you begin, ensure you have the following installed on your machine:
* [Python 3.xx.x](https://www.python.org/downloads/)
* A [TMDB API Key](https://developer.themoviedb.org/docs/getting-started)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourGitHubUsername/TmdbCLI.git
   cd TmdbCLI
   ```

2. **Create and activate a virtual environment:**
   * **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install requests
   ```

4. **Configure your API Key:**
   Open `tmdb_app.py` in your code editor and replace the `API_KEY` variable with your actual TMDB API key.

## Usage

Run the tool from your terminal by passing the `--type` argument followed by your desired movie category.

```bash
# Fetch currently playing movies
python tmdb_app.py --type "playing"

# Fetch popular movies
python tmdb_app.py --type "popular"

# Fetch top-rated movies
python tmdb_app.py --type "top"

# Fetch upcoming movies
python tmdb_app.py --type "upcoming"
```

## License
Distributed under the GPL-3.0 License. See `LICENSE` for more information.

## Authors
* **@Aloma007** 