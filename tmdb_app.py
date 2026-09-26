import argparse
import requests
import sys
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieves the key securely
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/movie"

def fetch_movies(movie_type):
    # 1. Map the CLI arguments to TMDB's exact endpoint names
    endpoints = {
        "playing": "now_playing",
        "popular": "popular",
        "top": "top_rated",
        "upcoming": "upcoming"
    }
    
    # Get the correct endpoint based on what user typed
    endpoint = endpoints[movie_type]
    url = f"{BASE_URL}/{endpoint}"
    
    # 2. Sets up the Query Parameters (including VIP pass)
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "page": 1
    }

    try:
        # 3. Makes the GET request to the server
        response = requests.get(url, params=params)
        
        # 4. Checks for HTTP errors (like a 401 Unauthorized or 404 Not Found)
        response.raise_for_status() 
        
        # 5. Converts the JSON response into a Python dictionary
        data = response.json()
        
        # 6. Loops through the results and display the top 5 movies
        print(f"\n--- {movie_type.upper()} MOVIES ---")
        
        # The movies are stored in a list under the key "results"
        movies = data.get("results", [])
        
        for movie in movies[:5]: 
            title = movie.get('title')
            rating = movie.get('vote_average')
            print(f"- {title} (Rating: {rating}/10)")
            
    # Handles network errors gracefully as requested by the project prompt
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from TMDB: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Fetch movie information from TMDB.")
    
    parser.add_argument(
        "--type", 
        type=str,
        choices=["playing", "popular", "top", "upcoming"],
        required=True,
        help="Specify the category of movies to fetch."
    )
    
    args = parser.parse_args()
    
    # Passes the user's choice to a new function
    fetch_movies(args.type)

if __name__ == "__main__":
    main()