# Import necessary libraries
import datetime
import webbrowser
import requests
import random

# -----------------------------------------------------------------------------
# CONFIGURATION - Personalize your assistant here!
# -----------------------------------------------------------------------------
ASSISTANT_NAME = "PyButler"

# Get your free API key from https://openweathermap.org/
WEATHER_API_KEY = "YOUR_API_KEY_HERE"  # <-- IMPORTANT: PASTE YOUR API KEY HERE
WEATHER_CITY = "London"              # City you want the weather for

# -----------------------------------------------------------------------------
# CORE FUNCTIONS - The building blocks of our assistant
# -----------------------------------------------------------------------------

def greet_user():
    """Greets the user at the start of the program."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    
    print(f"{greeting} I am {ASSISTANT_NAME}, your personal command-line assistant.")
    print("How can I help you today? (Type 'help' for commands)")
    print("-" * 50)

def get_time():
    """Returns the current date and time as a formatted string."""
    now = datetime.datetime.now()
    # Example format: "The current time is 10:30 PM on Saturday, October 26, 2024"
    time_str = now.strftime("The current time is %I:%M %p on %A, %B %d, %Y")
    return time_str

def get_weather(api_key, city):
    """Fetches and returns the weather for a given city using OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Construct the full URL with parameters
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(complete_url)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        weather_data = response.json()

        if weather_data["cod"] != 404:
            main_data = weather_data["main"]
            weather_desc = weather_data["weather"][0]["description"]
            
            temp = main_data["temp"]
            humidity = main_data["humidity"]
            
            return (
                f"The weather in {city.title()} is currently:\n"
                f"  - Temperature: {temp}°C\n"
                f"  - Description: {weather_desc.capitalize()}\n"
                f"  - Humidity: {humidity}%"
            )
        else:
            return "City not found. Please check the city name in the configuration."
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError:
        return "Could not parse weather data. The API response might have changed."

def open_website(url):
    """Opens a given URL in the default web browser."""
    try:
        webbrowser.open(url, new=2) # new=2 opens in a new tab, if possible
        return f"Opening {url}..."
    except Exception as e:
        return f"Could not open the website. Error: {e}"

def tell_joke():
    """Returns a random programming joke."""
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why did the CSS developer go to the hospital? He had a float.",
        "I would tell you a UDP joke, but you might not get it.",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "What's the object-oriented way to become wealthy? Inheritance."
    ]
    return random.choice(jokes)

def show_help():
    """Prints a list of available commands."""
    return """
Available commands:
  - time: Get the current date and time.
  - weather: Get the current weather for the configured city.
  - google: Open Google in your browser.
  - youtube: Open YouTube in your browser.
  - joke: Tell a random programming joke.
  - help: Show this list of commands.
  - exit / quit: Close the program.
    """

# -----------------------------------------------------------------------------
# MAIN PROGRAM LOOP - This is where the assistant listens for commands
# -----------------------------------------------------------------------------

def main():
    """The main function that runs the assistant's command loop."""
    greet_user()

    while True:
        # Get user input and convert it to lowercase for easier matching
        user_input = input("> ").lower().strip()

        if not user_input:
            continue

        # --- Command Processing ---
        if "time" in user_input:
            print(get_time())
        
        elif "weather" in user_input:
            if WEATHER_API_KEY == "YOUR_API_KEY_HERE":
                print("Error: Please set your OpenWeatherMap API key in the script.")
            else:
                print(get_weather(WEATHER_API_KEY, WEATHER_CITY))
                
        elif "google" in user_input:
            print(open_website("https://www.google.com"))

        elif "youtube" in user_input:
            print(open_website("https://www.youtube.com"))
            
        elif "joke" in user_input:
            print(tell_joke())
            
        elif "help" in user_input:
            print(show_help())

        elif user_input in ["exit", "quit", "bye"]:
            print(f"Goodbye! {ASSISTANT_NAME} is shutting down.")
            break
            
        else:
            print("Sorry, I don't understand that command. Type 'help' to see what I can do.")
        
        print("-" * 50) # Separator for clarity

# This standard line ensures that main() runs only when the script is executed directly
if __name__ == "__main__":
    main()