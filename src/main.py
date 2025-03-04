# Recommendation Program

import json
import time
import sys
from algorithms.search import search_recommendations
from utils.helpers import format_recommendations, validate_input

def get_recommendations(data, category):
    # Handle partial input
    for key in data["recommendations"].keys():
        if key.startswith(category):
            # Sort items by rating in descending order
            return sorted(data["recommendations"][key], key=lambda x: x.get("rating", 0), reverse=True)
    return []

def print_animated(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Load recommendations data
    with open('src/data/recommendations.json', 'r') as file:
        recommendations_data = json.load(file)

    # ASCII Art
    ascii_art = """
  ____                 _   _                 
 |  _ \ ___  __ _  ___| |_(_) ___  _ __  ___ 
 | |_) / _ \/ _` |/ __| __| |/ _ \| '_ \/ __|
 |  _ <  __/ (_| | (__| |_| | (_) | | | \__ \\
 |_| \_\___|\__,_|\___|\__|_|\___/|_| |_|___/
"""
    print_animated(ascii_art)
    print("Welcome to the Recommendation Program!")
    categories = list(recommendations_data["recommendations"].keys())

    while True:
        print("\nPlease select a category by entering the corresponding number (or 'exit' to quit):")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category.capitalize()}")

        user_input = input("\nEnter your choice: ").strip().lower()
        if user_input == 'exit':
            break

        try:
            choice = int(user_input)
            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                print(f"\nDetailed recommendations for {selected_category.capitalize()}:")
                detailed_recommendations = get_recommendations(recommendations_data, selected_category)
                for item in detailed_recommendations:
                    details = ", ".join(f"{key.capitalize()}: {value}" for key, value in item.items())
                    print(f"- {details}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to a category or 'exit' to quit.")

if __name__ == "__main__":
    main()